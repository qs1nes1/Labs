import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from minesweeper.model import Model
from minesweeper.controller import Controller
from minesweeper.view import *


@pytest.fixture
def app():
    """Create a QApplication instance for testing."""
    _app = QApplication([])
    yield _app
    _app.quit()


@pytest.fixture
def model():
    """Create a Model instance for testing."""
    _model = Model()
    yield _model


@pytest.fixture
def controller(model):
    """Create a Controller instance for testing."""
    _controller = Controller(model)
    yield _controller


@pytest.fixture
def view(controller, model, app):
    """Create a View instance for testing."""
    _view = View(controller, model)
    _view.show()
    yield _view
    _view.close()


def test_mousePressEvent(view, app):
    # Simulate a mouse press event at (0, 0) on the Field widget
    event = app.instance().postEvent(view.field, app.instance().QMouseEvent(
        app.instance().QEvent.MouseButtonPress, app.instance().QPoint(0, 0),
        Qt.LeftButton, Qt.LeftButton, Qt.NoModifier))
    assert event


def test_mouseReleaseEvent(view, app):
    # Simulate a mouse release event at (0, 0) on the Field widget
    event = app.instance().postEvent(view.field, app.instance().QMouseEvent(
        app.instance().QEvent.MouseButtonRelease, app.instance().QPoint(0, 0),
        Qt.LeftButton, Qt.LeftButton, Qt.NoModifier))
    assert event


def test_test_mouse_coordinates(view):
    # Test the test_mouse_coordinates method with valid coordinates
    assert view.field.test_mouse_coordinates(10, 10)  # Inside the field
    # Test the test_mouse_coordinates method with invalid coordinates
    assert not view.field.test_mouse_coordinates(1000, 1000)  # Outside the field


def test_paintEvent(view, app):
    # Test the paintEvent method
    event = app.instance().QPaintEvent()
    view.field.paintEvent(event)
    assert view.field.painter.isActive()


def test_create_menubar(view):
    # Test the create_menubar method
    assert view.menubar is not None
    assert view.gamemenu is not None
    assert len(view.gamemenu.actions()) == 4  # Including Exit action


def test_create_top_box(view):
    # Test the create_top_box method
    assert view.top_box is not None
    assert isinstance(view.top_box, TopBox)
    assert view.top_box.layout() is not None
    assert len(view.top_box.layout().children()) == 2  # TopPanel and Field


def test_create_top_panel(view):
    # Test the create_top_panel method
    assert view.top_box.top_panel is not None
    assert isinstance(view.top_box.top_panel, TopPanel)
    assert view.top_box.layout().indexOf(view.top_box.top_panel) == 0  # First in layout


def test_create_timer(view):
    # Test the create_timer method
    assert view.top_box.top_panel.timer is not None
    assert isinstance(view.top_box.top_panel.timer, Timer)


def test_run_timer(view):
    # Test the run_timer method
    view.top_box.top_panel.run_timer()
    assert view.top_box.top_panel.qtimer.isActive()


def test_stop_timer(view):
    # Test the stop_timer method
    view.top_box.top_panel.stop_timer()
    assert not view.top_box.top_panel.qtimer.isActive()


def test_clear_timer(view):
    # Test the clear_timer method
    view.top_box.top_panel.clear_timer()
    assert view.top_box.top_panel.timer.numbers[0].pixmap().toImage().isNull()  # Empty pixmap