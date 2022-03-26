# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

data_files = [
    ("seedsigner/resources/fonts", "resources/fonts"),
    ("seedsigner/resources/buttons", "resources/buttons"),
    ("seedsigner/resources/*.png", "resources"),
    ("settings.ini", "."),    
]

a = Analysis(['main.py'],
             pathex=['/home/skorn/venvs/seedsigner-gui/lib/python3.8/site-packages/cv2/cv2.abi3.so'],
             binaries=[],
             datas=data_files,
             hiddenimports=['PIL', 'PIL._imagingtk', 'PIL._tkinter_finder'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')