for testing
```bash
nix-repl
# or
nix-instantiate --eval <file.nix> --strict
```

attrset, attrset ?
//
rec set
list, ++
let in
attr access, with ... ; ...
inherit ... 
interpolated strings , ${...}


''
multi
line 
strings
''

paths relative vs abs
lookup path ~ angle brackets syntax
functions (single args, curried, attr set args, or named attr set args -> args@{a, b , ...})

builtins , i.e. primops
import -> import ./file.nix {a=1; b=8;}
pkgs.lib

derivations

