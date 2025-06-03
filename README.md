# idl-lib-renderers-py

**🐍 Solana Python Program Clients Library 🐍**

Solana Python program clients generated from [solana-idl-lib](https://github.com/bitquery/solana-idl-lib), using [codama python renderers](https://github.com/codama-idl/codama). 

It shows how to generate Python-based SDKs from Anchor IDLs, used for Solana client interaction in Python.

## 📓 Usage in Jupyter Notebook

You can explore usage examples in:

- `notebooks/pump.ipynb`
- `notebooks/jup.ipynb`

It shows:

- How to construct and simulate transactions
- How to parse program accounts
- How to use the generated Python client for Solana program interactions


## 📦 Generate Python clients from IDL
```
from codama import createFromRoot, renderPythonVisitor
from solana_idl_lib import rootNodeFromAnchor

def GenIdl(file: str, dirPath: str):
    anchorIdl = require(file)
    rootNode = rootNodeFromAnchor(anchorIdl)
    codama = createFromRoot(rootNode)
    codama.accept(renderPythonVisitor(dirPath))

GenIdl("./idls/pump.json", "pump")
GenIdl("./idls/idl-0.1.2.json", "Lifinity")
```


## 🤝 Contribution

Contributed by [daog1](https://github.com/daog1) from [Solar](https://www.solar.team/).

Originated from [PyGenIDL001](https://github.com/daog1/PyGenIDL001)

Feel free to raise issues or submit PRs for future improvements.

