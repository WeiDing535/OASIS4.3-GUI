# Contributing

Please open an issue before a large scientific change. A contribution should state the crystallographic assumption, provide a synthetic or redistributable regression case, and report the command used for validation. Do not commit unpublished target structures, private diffraction data, credentials, local paths or CCP4/Parrot application source.

Run `pytest -m 'not reference_data'` and `python tools/check_release.py` before submitting a change. New algorithms should be opt-in until benchmark evidence shows that they are safe as defaults.
