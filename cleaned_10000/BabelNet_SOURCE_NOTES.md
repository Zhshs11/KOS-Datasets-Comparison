# BabelNet source notes

The workbook contains 10,000 unique child-parent pairs. Original `hypernym`, `hyponym` and `subclass_of` directions are retained alongside normalized child/parent fields. The notes sheet documents cleaning, sampling and record-level provenance.

- Relations: [THUNLP BabelNet-Sememe-Prediction](https://github.com/thunlp/BabelNet-Sememe-Prediction/tree/df580cdebd341c4a2d8e9190bfe36c6282cfd427), `data-all/entity2id.txt`, `relation2id.txt` and `train2id.txt`.
- Display labels and definitions: [THUNLP MSGI](https://github.com/thunlp/MSGI/tree/3bb7c7f4a10d73feed84042ea7239d5a668b4690), `data.zip` / `data/babel_data_full.txt`. The first English synonym is used as a display label, not asserted to be an official preferred label.
- The source publications do not specify a BabelNet release. This is a research subset, not a full or statistically representative BabelNet export.

The source repository's MIT notice is reproduced below. It does not establish a blanket licence for BabelNet, MSGI or their upstream resources. MSGI has no separate LICENSE file in the referenced snapshot. [BabelNet's terms](https://babelnet.org/full-license) and upstream rights remain applicable; consult them before reuse or redistribution.

## BabelNet-Sememe-Prediction repository notice

```text
MIT License

Copyright (c) 2019 THUNLP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
