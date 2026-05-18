# Nix language cheatsheet

## Testing snippets

```bash
nix repl                              # interactive
nix-instantiate --eval file.nix --strict
```

## Attribute sets

```nix
{ a = 1; b = "two"; }                 # attrset
{ a = 1; } ? a                        # has-attr  → true
{ a = 1; b = 2; } // { b = 9; c = 3; } # merge (rhs wins) → { a=1; b=9; c=3; }
rec { x = 1; y = x + 1; }             # rec: recursive self-reference 
```

## Lists

```nix
[ 1 2 3 ] ++ [ 4 5 ]                  # → [ 1 2 3 4 5 ]
```

## let / with / inherit / attr access

```nix
let x = 1; y = 2; in x + y            # let..in
let s = { a = 1; }; in with s; a + 1  # with: bring attrs into scope
let a = 1; b = 2; in { inherit a b; } # inherit: shorthand for a = a; b = b;
({ a = { b = 1; }; }).a.b              # attr access → 1
```

## Strings

```nix
"hello ${name}"                       # interpolation
''
multi
line
''                                    # multi-line; leading indent stripped
```

## Paths

```nix
./file.nix                            # relative (resolved at parse time)
/etc/nixos                            # absolute
<nixpkgs>                             # lookup path (uses $NIX_PATH)
```

## Functions

```nix
x: x + 1                              # single arg
x: y: x + y                           # curried
{ a, b }: a + b                       # attr-set arg
{ a, b ? 0, ... }: a + b              # with default + ignore extras
args@{ a, b, ... }: args.a + b        # @-pattern: bind whole set
```

## Builtins (primops)

```nix
builtins.length [ 1 2 3 ]             # → 3
builtins.toJSON { a = 1; }            # → "{\"a\":1}"
```

## Import

```nix
import ./file.nix { a = 1; b = 8; }   # eval file, apply as function
```

## pkgs.lib
**updating registry entries should happen with `nix registry` then `nix flake update`**
```nix
let pkgs = import <nixpkgs> {};
in pkgs.lib.strings.toUpper "abc"     # → "ABC"
```
 

## Derivations

```nix
{ pkgs ? import <nixpkgs> {} }:
pkgs.stdenv.mkDerivation {
  pname   = "hello-world";
  version = "0.1";
  src     = ./.;
  buildPhase   = "echo hi > hello";
  installPhase = "install -Dm644 hello $out/hello";
}
```


## Flake.nix
an attrset with `inputs` and `outputs` keys, 
`inputs` is an attrset `outputs` a function

`nix-rebuild switch` uses the configuration from outputs
