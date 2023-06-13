# -*- mode: python ; coding: utf-8 -*-
import sys; sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

a = Analysis(
    ['index.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('creditos.html', '.'),       # Agregar archivos al ejecutable
        ('info.html', '.'),
        ('link.txt', '.'),
        ('eq.csv', '.'),
        ('modelo_ecuaciones.joblib', '.'),
    ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtWidgets',
        'PyQt5.QtGui',
        'PyQt5.QtCore',
        'webbrowser',
        'sympy',
        'numpy',
        're',
        'math',
        'sklearn',
        'sklearn.feature_extraction',
        'sklearn.feature_extraction.text',
        'joblib',
        'csv',
        'os',
        'sys',
        'sklearn.naive_bayes',
        'scikit-learn',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='index',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='index',
)