from flask import Blueprint, request, jsonify
from backend.repository.repository import PostureDataRepository
from backend.db.model import PostureData