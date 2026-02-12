"""
REST API Server pentru UBB Discord Bot
v2.0.0 Feature - Flask API cu endpoints complete
"""

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)

# Configurare
app.config['JSON_SORT_KEYS'] = False

# Functii ajutoare
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != os.getenv('API_KEY', 'ubb-bot-secret-key'):
            return jsonify({"error": "Invalid API key"}), 401
        return f(*args, **kwargs)
    return decorated

def load_json_file(filename):
    """Incarca un fisier JSON"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HEALTH CHECK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "online",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# STATS ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/stats/user/<user_id>', methods=['GET'])
def get_user_stats(user_id):
    """Obtine statistici pentru un utilizator"""
    stats = load_json_file('data/user_stats.json')
    
    if user_id not in stats:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "user_id": user_id,
        "stats": stats[user_id],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/v1/stats/leaderboard', methods=['GET'])
def get_leaderboard():
    """Obtine leaderboard-ul global"""
    stats = load_json_file('data/user_stats.json')
    
    # Sorteaza dupa XP
    sorted_users = sorted(
        stats.items(),
        key=lambda x: x[1].get('experience', 0),
        reverse=True
    )[:10]
    
    leaderboard = [
        {
            "rank": idx + 1,
            "user_id": user_id,
            "experience": stats[user_id].get('experience', 0),
            "level": stats[user_id].get('level', 1)
        }
        for idx, (user_id, stats) in enumerate(sorted_users)
    ]
    
    return jsonify({
        "leaderboard": leaderboard,
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ECONOMY ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/economy/balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    """Obtine balanta unui utilizator"""
    economy = load_json_file('data/economy.json')
    
    if user_id not in economy:
        return jsonify({
            "user_id": user_id,
            "balance": 0,
            "items": []
        })
    
    return jsonify({
        "user_id": user_id,
        "balance": economy[user_id].get('balance', 0),
        "items": economy[user_id].get('items', {}),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/v1/economy/shop', methods=['GET'])
def get_shop():
    """Obtine lista shop-ului"""
    shop = load_json_file('data/shop.json')
    
    return jsonify({
        "shop": shop,
        "total_items": len(shop),
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LOGS ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/logs/server/<server_id>', methods=['GET'])
@require_api_key
def get_server_logs(server_id):
    """Obtine logurile unui server"""
    logs = load_json_file('data/server_logs.json')
    
    if server_id not in logs:
        return jsonify({
            "server_id": server_id,
            "logs": []
        })
    
    limit = request.args.get('limit', 50, type=int)
    server_logs = logs[server_id][-limit:]
    
    return jsonify({
        "server_id": server_id,
        "logs": server_logs,
        "total": len(logs.get(server_id, [])),
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RANKS ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/ranks/user/<user_id>', methods=['GET'])
def get_user_rank(user_id):
    """Obtine rank-ul unui utilizator"""
    stats = load_json_file('data/user_stats.json')
    
    if user_id not in stats:
        return jsonify({"error": "User not found"}), 404
    
    xp = stats[user_id].get('experience', 0)
    
    rank_tiers = [
        {"level": 1, "name": "Noob", "emoji": "🥚", "xp_required": 0},
        {"level": 2, "name": "Learner", "emoji": "🐣", "xp_required": 100},
        {"level": 3, "name": "Student", "emoji": "📚", "xp_required": 300},
        {"level": 4, "name": "Scholar", "emoji": "🎓", "xp_required": 600},
        {"level": 5, "name": "Master", "emoji": "⚡", "xp_required": 1000},
        {"level": 6, "name": "Legend", "emoji": "👑", "xp_required": 1500},
        {"level": 7, "name": "Mythical", "emoji": "🌟", "xp_required": 2500},
        {"level": 8, "name": "Godlike", "emoji": "🔱", "xp_required": 5000},
    ]
    
    current_rank = None
    for rank in reversed(rank_tiers):
        if xp >= rank["xp_required"]:
            current_rank = rank
            break
    
    next_rank = None
    for rank in rank_tiers:
        if rank["xp_required"] > xp:
            next_rank = rank
            break
    
    return jsonify({
        "user_id": user_id,
        "current_rank": current_rank,
        "next_rank": next_rank,
        "xp": xp,
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GAME STATS ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/games/stats/<user_id>', methods=['GET'])
def get_game_stats(user_id):
    """Obtine statistici de jocuri pentru un utilizator"""
    game_stats = load_json_file('data/game_stats.json')
    
    if user_id not in game_stats:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "user_id": user_id,
        "gamestats": game_stats[user_id],
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANALYTICS ENDPOINTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/api/v1/analytics/summary', methods=['GET'])
@require_api_key
def get_analytics_summary():
    """Obtine sumar analytics"""
    stats = load_json_file('data/user_stats.json')
    economy = load_json_file('data/economy.json')
    game_stats = load_json_file('data/game_stats.json')
    
    total_users = len(stats)
    total_xp = sum(user.get('experience', 0) for user in stats.values())
    total_coins = sum(user.get('balance', 0) for user in economy.values())
    total_games_played = sum(
        sum(game.get('total', 0) for game in user.values())
        for user in game_stats.values()
    )
    
    return jsonify({
        "total_users": total_users,
        "total_xp": total_xp,
        "average_xp_per_user": total_xp / max(total_users, 1),
        "total_coins_in_economy": total_coins,
        "total_games_played": total_games_played,
        "timestamp": datetime.now().isoformat()
    })

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ERROR HANDLERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
