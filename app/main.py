from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from repositories import giochi_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)

@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    games: list[dict] = giochi_repository.get_all_games()

    # 2. Passiamo la variabile 'games' al template
    return render_template("index.html", games=games)