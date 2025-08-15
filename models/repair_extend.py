from odoo import models, fields, api


class RepairOrder(models.Model):
    _inherit = 'repair.order'

    expense_account_id = fields.Many2one(
        'account.account',
        string="Expense Account",
        required=True,
        help="Select the expense account related to this repair order."
    )

    analytic_distribution_model_id = fields.Many2one(
        'account.analytic.distribution.model',
        string="Analytic Distribution",
        required=True,
        help="Select the analytic distribution model. Will be auto-filled if expense account matches a model prefix."
    )

    @api.onchange('expense_account_id')
    def _onchange_expense_account(self):
        """Auto-fill Analytic Distribution Model based on Expense Account prefix."""
        self.analytic_distribution_model_id = False

        if self.expense_account_id and self.expense_account_id.code:
            dist = self.env['account.analytic.distribution.model'].search(
                [('account_prefix', '=like',
                  f"{self.expense_account_id.code}%")],
                limit=1
            )
            if dist:
                self.analytic_distribution_model_id = dist
