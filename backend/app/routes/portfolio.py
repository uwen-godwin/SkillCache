from flask import Blueprint, jsonify, request
from ..models import Portfolio, db

bp = Blueprint('portfolio', __name__)

@bp.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    portfolio = Portfolio.query.first()
    if portfolio:
        return jsonify({
            'title': portfolio.title,
            'description': portfolio.description
        })
    return jsonify({'error': 'No portfolio found'}), 404

@bp.route('/api/portfolio', methods=['POST'])
def update_portfolio():
    data = request.json
    portfolio = Portfolio.query.first()
    if portfolio:
        portfolio.title = data['title']
        portfolio.description = data['description']
    else:
        portfolio = Portfolio(title=data['title'], description=data['description'])
        db.session.add(portfolio)
    db.session.commit()
    return jsonify({'message': 'Portfolio updated successfully'})
