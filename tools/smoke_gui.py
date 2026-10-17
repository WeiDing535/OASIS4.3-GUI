"""Construct the GUI without entering its event loop."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6 import QtCore, QtGui, QtWidgets
from oasis_py import __product__
from oasis_py.gui import make_window

app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
window = make_window(QtCore, QtGui, QtWidgets)
assert __product__ in window.windowTitle()
assert window.sequence is not None
assert window.copies.minimum() == 1
assert window.solvent.isReadOnly()
assert len(window.help_buttons) >= 20
window.close()
print("GUI smoke test passed:", __product__)
