from odoo import http
from odoo.http import request

class TestThemeController(http.Controller):

    @http.route('/', type='http', auth="public", website=True)
    def homepage(self, **kw):
        return request.render("theme_elearning.test_page_template")
