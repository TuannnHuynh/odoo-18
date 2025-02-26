from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    opening_date = fields.Date(string="Ngày khai giảng")
    level = fields.Selection(
        [
            ('basic', 'Cơ bản'),
            ('intermediate', 'Cơ bản - Trung cấp'),
            ('advanced', 'Cao cấp')
        ],
        string="Trình độ"
    )
    study_days = fields.Selection(
        [
            ('mon_wed_fri', 'Thứ 2, Thứ 4, Thứ 6'),
            ('tue_thu', 'Thứ 3, Thứ 5'),
            ('weekend', 'Thứ 7, Chủ Nhật')
        ],
        string="Lịch học"
    )
    study_time = fields.Selection(
        [
            ('morning', '08:00 - 11:00'),
            ('afternoon', '13:30 - 16:30'),
            ('evening', '18:30 - 21:00')
        ],
        string="Giờ học"
    )

    def get_study_days_label(self):
        """Trả về label của 'study_days' thay vì value"""
        return dict(self._fields['study_days'].selection).get(self.study_days, 'Không xác định')

    def get_level_label(self):
        """Trả về label của 'level'"""
        return dict(self._fields['level'].selection).get(self.level, 'Không xác định')

    def get_study_time_label(self):
        """Trả về label của 'study_time'"""
        return dict(self._fields['study_time'].selection).get(self.study_time, 'Không xác định')