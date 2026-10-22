#!/usr/bin/env python3
"""Read-only preflight. No builds, version commands, network or device queries."""
import argparse
import json
import platform
import shutil
from pathlib import Path


def inspect(root: Path) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError('La raíz debe ser una carpeta existente')
    names = ['AGENTS.md', 'docs/PROJECT_STATUS.md', 'Package.swift', 'Package.resolved',
             '.swift-version', 'Build_DMG.command', 'README.md']
    tools = ['swift', 'swiftc', 'xcodebuild', 'xcrun', 'codesign', 'hdiutil', 'python3', 'git']
    children = list(root.iterdir())
    projects = sorted(p.name for p in children if p.suffix in {'.xcodeproj', '.xcworkspace'} and p.is_dir())
    return {
        'root': str(root),
        'host_os': platform.system(),
        'host_architecture': platform.machine(),
        'instruction_candidates_present': [name for name in names if (root / name).is_file()],
        'top_level_xcode_projects': projects,
        'tools_on_path': {name: bool(shutil.which(name)) for name in tools},
        'apple_sdk_readiness': 'NOT_VERIFIED',
        'build_tests_devices': 'NOT_RUN',
        'note': 'Disponibilidad en PATH no verifica SDK, licencias, versión, firma, simuladores ni dispositivos. Leer instrucciones antes de ejecutar.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.root), ensure_ascii=False, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
