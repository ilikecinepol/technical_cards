# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/PythonCode/card_generator 2.0/generator.py'],
             pathex=['D:\\PythonCode\\card_generator 2.0'],
             binaries=[],
             datas=[('D:/PythonCode/card_generator 2.0/files', 'files/'), ('D:/PythonCode/card_generator 2.0/profiles', 'profiles/'), ('D:/PythonCode/card_generator 2.0/Техкарты готовые', 'Техкарты готовые/'), ('D:/PythonCode/card_generator 2.0/READ_ME.pdf', '.')],
             hiddenimports=[],
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
          name='generator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='D:\\PythonCode\\card_generator 2.0\\Лого2.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='generator')
