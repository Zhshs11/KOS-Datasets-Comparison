"""Build the published selection record from its two UTF-8 CSV tables.

Requires python-docx 1.2.0. All inputs are local. No network calls are made.
"""
import csv
import json
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION_START, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT = Path(__file__).resolve().parent
FILENAME = "Knowledge_Resource_Selection_Process_224_to_20.docx"
FONT = "Times New Roman"
BOOKMARK = 0

def records(filename):
    with (ROOT / filename).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

screen = records("screening.csv")
panel = records("panel_selection.csv")
summary = json.loads((ROOT / "selection_summary.json").read_text(encoding="utf-8"))
families = summary["families"]
source_urls = {r["resource_id"]: r["source_url"] for r in screen}

doc = Document()
for name in ("Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Caption"):
    s = doc.styles[name]
    s.font.name = FONT
    s.font.color.rgb = RGBColor(0, 0, 0)
    fonts = s._element.get_or_add_rPr().get_or_add_rFonts()
    for attr in list(fonts.attrib):
        if attr.endswith("Theme"):
            del fonts.attrib[attr]
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn("w:" + key), FONT)
    ppr = s._element.find(qn("w:pPr"))
    if ppr is not None:
        for border in list(ppr.findall(qn("w:pBdr"))):
            ppr.remove(border)
normal = doc.styles["Normal"]
normal.font.size = Pt(11)
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.08
normal.paragraph_format.widow_control = True
for name, size in (("Title", 19), ("Subtitle", 11), ("Heading 1", 12), ("Heading 2", 11)):
    s = doc.styles[name]
    s.font.size = Pt(size)
    s.paragraph_format.keep_with_next = True
    s.paragraph_format.space_before = Pt(10 if name.startswith("Heading") else 0)
    s.paragraph_format.space_after = Pt(6)
doc.styles["Title"].font.bold = False
doc.styles["Heading 1"].font.bold = True
doc.styles["Heading 2"].font.bold = True
doc.styles["Caption"].font.size = Pt(10.5)
doc.styles["Caption"].font.italic = False
doc.styles["Caption"].paragraph_format.keep_with_next = True

def section_geometry(section, landscape=False):
    section.orientation = WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
    section.page_width = Inches(11.6931 if landscape else 8.2681)
    section.page_height = Inches(8.2681 if landscape else 11.6931)
    section.left_margin = section.right_margin = Inches(0.65)
    section.top_margin = section.bottom_margin = Inches(0.60)
    section.header_distance = section.footer_distance = Inches(0.27)

section_geometry(doc.sections[0])
footer = doc.sections[0].footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = footer.add_run("Knowledge Resource Selection  |  ")
r.font.size = Pt(9)
for instr in ("PAGE", "NUMPAGES"):
    if instr == "NUMPAGES":
        footer.add_run(" / ").font.size = Pt(9)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    footer._p.append(fld)

def para(text, style=None):
    p = doc.add_paragraph(text, style)
    return p

def heading(text):
    return para(text, "Heading 1")

def fieldrun(p, text, bold=False, size=10):
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    return r

def hyperlink(p, text, url=None, anchor=None, size=10):
    h = OxmlElement("w:hyperlink")
    if url:
        h.set(qn("r:id"), p.part.relate_to(url, RT.HYPERLINK, is_external=True))
    else:
        h.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r")
    pr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    for key in ("ascii", "hAnsi", "eastAsia"):
        fonts.set(qn("w:" + key), FONT)
    pr.append(fonts)
    color = OxmlElement("w:color"); color.set(qn("w:val"), "204A70"); pr.append(color)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); pr.append(sz)
    r.append(pr)
    t = OxmlElement("w:t"); t.text = text; r.append(t); h.append(r)
    p._p.append(h)

def bookmark(p, name):
    global BOOKMARK
    BOOKMARK += 1
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(BOOKMARK)); start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd"); end.set(qn("w:id"), str(BOOKMARK))
    p._p.insert(0, start); p._p.append(end)

def anchor(prefix, rid):
    return prefix + "_" + rid.replace("-", "_")

def shade(cell, color):
    pr = cell._tc.get_or_add_tcPr()
    el = pr.find(qn("w:shd"))
    if el is None: el = OxmlElement("w:shd"); pr.append(el)
    el.set(qn("w:fill"), color)

def style_cell(cell, header=False, center=False):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    for p in cell.paragraphs:
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.keep_with_next = False
        p.paragraph_format.widow_control = True
        if center: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(10 if not header else 10)
            r.font.bold = header
            r.font.color.rgb = RGBColor(0,0,0)
    if header: shade(cell, "E9EDF1")

def table(headers, widths):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for c,w in zip(t.columns, widths): c.width = Inches(w)
    pr = t._tbl.tblPr
    layout = pr.find(qn("w:tblLayout"))
    if layout is None: layout = OxmlElement("w:tblLayout"); pr.append(layout)
    layout.set(qn("w:type"), "fixed")
    borders = OxmlElement("w:tblBorders")
    for side in ("top","left","bottom","right","insideH","insideV"):
        b = OxmlElement("w:" + side); b.set(qn("w:val"),"single")
        b.set(qn("w:sz"),"4"); b.set(qn("w:color"),"D9D9D9"); borders.append(b)
    pr.append(borders)
    margins = OxmlElement("w:tblCellMar")
    for side,val in (("top",65),("bottom",65),("left",75),("right",75)):
        x = OxmlElement("w:" + side); x.set(qn("w:w"),str(val)); x.set(qn("w:type"),"dxa"); margins.append(x)
    pr.append(margins)
    for cell,txt,w in zip(t.rows[0].cells,headers,widths):
        cell.width = Inches(w); cell.text=txt; style_cell(cell,True)
    trpr=t.rows[0]._tr.get_or_add_trPr()
    trpr.append(OxmlElement("w:tblHeader"))
    trpr.append(OxmlElement("w:cantSplit"))
    return t

def row(t, vals, widths, centers=()):
    rr=t.add_row()
    rr._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    for i,(c,v,w) in enumerate(zip(rr.cells, vals, widths)):
        c.width=Inches(w);c.text=v;style_cell(c,center=i in centers)
    return rr

def band(t, text):
    rr=t.add_row()
    cell=rr.cells[0].merge(rr.cells[-1]); cell.text=text;shade(cell,"E9EDF1")
    style_cell(cell)
    for p in cell.paragraphs:
        p.paragraph_format.keep_with_next=True
        for r in p.runs:r.bold=True
    rr._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    return rr

title=para("Knowledge Resource Selection\nfrom 224 Resources to 20 Candidates","Title")
title.alignment=WD_ALIGN_PARAGRAPH.CENTER
sub=para("Supplementary screening and comparative selection record","Subtitle")
sub.alignment=WD_ALIGN_PARAGRAPH.CENTER
p=para("Version 1.0");p.alignment=WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after=Pt(12)
para("We document the recorded screening of 224 knowledge resources and the selection of a 20-resource panel for subsequent within-family assessment. The screening sequence retained 99 resources after the scope check, 88 after the English-content check, and 77 after the public-access check. The final panel was drawn from these 77 resources through a qualitative comparative design.")
para("The record covers five families of knowledge organization systems (KOSs). Stable resource identifiers connect the screening decisions in Table S2 with the panel decisions in Table S3. Resource names link to the source pointers retained in the discovery catalog.")

heading("I Recorded eligibility screening")
para("We reconstruct the recorded decisions in the order scope, English content, and public access. S1 requires general-purpose or cross-domain content. S2 requires usable English semantic content; an English introduction alone does not establish eligibility, while a multilingual resource may qualify. S3 requires an accepted free route to actual resource content. The recorded access policy permits free registration, free academic access under applicable licenses, and explicitly bounded public subsets or historical releases.")
para("Pass denotes a condition supported in the screening audit. Fail denotes a recorded failure. Unverified denotes insufficient established evidence. A dash marks a check not reached in this reconstruction. We assign each non-advancing resource to its first non-pass condition, so later recorded issues do not count the same resource again.")
para("The 147 non-advancing resources comprise 125 scope failures, 11 English-content non-passes, and 11 public-access non-passes. Each of the latter two groups contains one recorded failure and ten unverified cases. Thus, 127 entries have a recorded failure and 20 stop because evidence was unverified.")
para("Table S1. Counts retained at each stage","Caption")
w=[2.35,.59,.64,.70,.70,.80,1.18]
t=table(["Family","Initial","S1\nscope","S2\nEnglish","S3\naccess","Selected","Alternatives"],w)
for f,x in families.items():
    row(t,[f+"  "+x["name"],*[str(x[k]) for k in ("identified","after_scope","after_english","after_access","selected","alternatives")]],w,range(1,7))
rr=row(t,["Total","224","99","88","77","20","57"],w,range(1,7))
for c in rr.cells:
    for p in c.paragraphs:
        for r in p.runs:r.bold=True
para("S1-S3 show cumulative retained counts. The last two columns partition the 77 resources that passed all three recorded checks.").paragraph_format.space_before=Pt(5)

p=heading("II Comparative panel selection")
p.paragraph_format.page_break_before=True
para("We adopted a 20-resource panel as a purposive comparative design drawn from the 77 advancing resources. Three considerations guided the recorded rationale: contrasts in knowledge organization, informative relationships between source and derivative or integrated resources, and a bounded allocation across the five families.")
para("Organizational contrast covers subject classification, controlled terminology, formal and frame-based modeling, knowledge graphs, and lexical semantics. Source relationships remain explicit because a resource derived from another may provide a distinct organizational design. The recorded allocation is four resources in F1, three in F2, three in F3, six in F4, and four in F5.")
para("These considerations describe the adopted comparison design. They are applied jointly rather than as numerical scores or sequential eligibility gates. Table S3 records the rationale for each resource. The 57 resources outside the panel remain documented alternatives; their status does not establish inferiority or ineligibility. The 20 selected resources are candidates for subsequent within-family assessment, rather than established family winners.")
para("The selected panel consists of:")
for f,x in families.items():
    names="; ".join(r["resource_name"] for r in panel if r["family_id"]==f and r["panel_status"]=="Selected")
    p=para(f'{f}  {x["name"]} ({x["selected"]}): {names}.')
    p.paragraph_format.space_after=Pt(5)

heading("III Provenance and reproducibility")
para("The discovery catalog [1] identifies the initial resources. The screening audit [2] supplies the recorded eligibility decisions and qualifications. This supplement records the final panel and its resource-level reasons in Table S3. It consolidates these records without introducing a new source audit or a new performance evaluation.")
para("The linked resource pages reproduce pointers from the catalogs and have not been revalidated for this release. Each recorded public route applies only to the stated resource or subset. For example, the DDC entry concerns public DDC 22 three-level summaries, and the UDC entry concerns the UDC Summary. Neither entry establishes access to the corresponding complete classification.")
para("The accompanying screening.csv and panel_selection.csv preserve the 224 screening records and 77 panel decisions. The validation script checks identifiers, stage counts, panel membership, and the accounting identity below. These files allow readers to reconstruct the documented decisions and counts. Independent reassessment of resource eligibility requires the underlying source evidence; the qualitative panel design does not uniquely determine the 20 resources through an algorithm.")
para("224 = 125 scope non-passes + 11 English non-passes + 11 access non-passes + 57 panel alternatives + 20 selected resources.")
heading("Source records")
para("[1] KOS_Candidate_Catalog_en.xlsx. Candidate catalog. Original resource identifiers and discovery pointers.")
para("[2] KOS_Candidate_Catalog_after_en.xlsx. Screening decisions and Candidate catalog. Recorded eligibility decisions and resource-specific boundaries.")
para("Source filenames identify the underlying records. The companion CSV files expose the decisions reported in this supplement; they do not replace the original discovery search log or source snapshots.")

sec=doc.add_section(WD_SECTION_START.NEW_PAGE);section_geometry(sec,True)
heading("IV Resource level eligibility decisions")
para("Table S2. Initial resources and recorded screening decisions","Caption")
para("S1 = broad scope; S2 = usable English content; S3 = accepted public access. A dash means the check was not reached. Advance links lead to the corresponding Table S3 record. Resource-name links retain the discovery catalog's source pointers.")
w=[.70,2.44,.61,.80,.80,.95,4.09]
t=table(["Resource\nID","Initially identified resource [1]","S1\nScope","S2\nEnglish","S3\nAccess","Screening\noutcome","Recorded basis and scope limitation [2]"],w)
for f,x in families.items():
    band(t,f'{f}  {x["name"]}  |  {x["identified"]} initial; {x["after_scope"]} after S1; {x["after_english"]} after S2; {x["after_access"]} advance')
    for rr in (r for r in screen if r["family_id"]==f):
        vals=[rr["resource_id"],"",*[("—" if rr[k]=="Not assessed" else rr[k]) for k in ("s1_scope","s2_english","s3_public_access")],"",rr["decision_basis"]]
        r=row(t,vals,w,(2,3,4,5))
        bookmark(r.cells[0].paragraphs[0],anchor("screen",rr["resource_id"]))
        hyperlink(r.cells[1].paragraphs[0],rr["resource_name"],url=rr["source_url"])
        if rr["screening_outcome"]=="Advance":
            hyperlink(r.cells[5].paragraphs[0],"Advance",anchor=anchor("panel",rr["resource_id"]))
        else:
            fieldrun(r.cells[5].paragraphs[0],"Not advanced")
band(t,"Total: 224 resources; 77 advance to panel selection; 147 stop at their first recorded non-pass condition.")

sec=doc.add_section(WD_SECTION_START.NEW_PAGE);section_geometry(sec,True)
heading("V Resource level panel decisions")
para("Table S3. Comparative selection from 77 resources to the 20-resource panel","Caption")
para("Organizational contrasts, source relationships, and panel rationales document the qualitative design described in Section II. Selected identifies a panel member. Alternative identifies an advancing resource outside this panel. Resource IDs link back to Table S2.")
w=[.70,1.32,1.70,2.57,3.25,.85]
t=table(["Resource\nID","Resource","Organizational\ncontrast","Source relationships and boundaries","Panel allocation and rationale","Panel\nstatus"],w)
for f,x in families.items():
    band(t,f'{f}  {x["name"]}  |  {x["after_access"]} advancing; {x["selected"]} selected; {x["alternatives"]} alternatives')
    for rr in (r for r in panel if r["family_id"]==f):
        r=row(t,["",rr["resource_name"],rr["organizational_contrast"],rr["relationship_and_boundary"],rr["panel_reason"],rr["panel_status"]],w,(5,))
        bookmark(r.cells[0].paragraphs[0],anchor("panel",rr["resource_id"]))
        hyperlink(r.cells[0].paragraphs[0],rr["resource_id"],anchor=anchor("screen",rr["resource_id"]))
        if rr["panel_status"]=="Selected":
            for c in r.cells:shade(c,"F2F5F8")
band(t,"Total: 77 advancing resources; 20 selected for subsequent assessment; 57 documented alternatives.")

props=doc.core_properties
props.title="Knowledge Resource Selection from 224 Resources to 20 Candidates"
props.subject="Recorded eligibility screening and comparative panel selection"
props.author=""
props.last_modified_by=""
props.keywords="knowledge organization systems; resource selection; eligibility screening; reproducibility"
props.comments=""
props.version="1.0"
doc.save(ROOT/FILENAME)
print(ROOT/FILENAME)

