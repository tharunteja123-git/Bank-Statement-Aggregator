from .statement_controller import statement_bp
from .user_controller import user_bp
from .company_controller import company_bp
from .branch_controller import branch_bp


def register_controllers(app):
    """
    Registers the blueprints for different controllers in the Flask app.

    Parameters:
    - app: The Flask app object.

    Returns:
    None
    """
    app.register_blueprint(statement_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(branch_bp)
