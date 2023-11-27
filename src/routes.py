from flask import Flask, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError, PendingRollbackError, NoResultFound
from models import session, Base, URLMapping, engine
from methods import check_valid_url

def create_app(_session):
    app = Flask(__name__)

    @app.route('/create-short-url', methods=['POST'])
    def create_shor_url():
        try:
            original_url = request.form.get('original_url')
            short_url = request.form.get('short_url')

            if not original_url or not short_url:
                return 'Вы не указали изначальный URL или его короткую версию', 403

            isvalid = check_valid_url(original_url)

            if not isvalid:
                return 'Вы ввели не корректный изначальный URL', 403

            new_url = URLMapping(original_url=original_url, short_url=short_url)

            _session.add(new_url)
            _session.commit()

            return jsonify(new_url.to_json())

        except (IntegrityError, PendingRollbackError):
            _session.rollback()
            return 'Этот короткий url, занят', 403

    @app.route('/<short_url>', methods=['GET'])
    def get_site_with_shor_url(short_url: str):
        info_about_url = _session.query(URLMapping).filter(URLMapping.short_url == short_url).first()

        if not info_about_url:
            return 'Сайт не найден', 404

        return redirect(info_about_url.original_url)

    return app


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app = create_app(session)
    app.run()
