import zipapp

zipapp.create_archive(
    source='.',                    # Package everything in this folder
    target='files_cutter.pyz',     # Output file
    interpreter='/usr/bin/env python3'  # Cross-platform interpreter line
)
