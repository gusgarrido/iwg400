{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  inputs.pyproject-nix.url = "github:pyproject-nix/pyproject.nix";
  inputs.pyproject-nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs = { nixpkgs, pyproject-nix, ... } :
    let
      project = pyproject-nix.lib.project.loadPyproject { projectRoot = ./.; };
      requirements = pyproject-nix.lib.project.loadRequirementsTxt { projectRoot = ./.; };

      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
      python = pkgs.python314;
    in {
      devShells.${system}.default =
        let
          pythonEnv = python.withPackages ( requirements.renderers.withPackages { inherit python; } );
        in
        pkgs.mkShell { packages = [
          pkgs.pyright
          
          pythonEnv
          python.pkgs.black
          python.pkgs.isort
        ]; };

      packages.${system}.default =
        let
          attrs = project.renderers.buildPythonPackage { inherit python; };
        in
        python.pkgs.buildPythonPackage (attrs);
    };
}