from odoo import models, fields, api


class RepairOrder(models.Model):
    _inherit = 'repair.order'

    expense_account_id = fields.Many2one(
        'account.account',
        string="Expense Account",
        required=True,
    )

    analytic_distribution_id = fields.Many2one(
        'account.analytic.account',
        string="Analytic Distribution",
        compute='_compute_analytic_distribution',
        store=True,
        readonly=True,
    )

    @api.depends('expense_account_id')
    def _compute_analytic_distribution(self):
        """
        Dynamically fetch the analytic distribution based on the expense account's code
        using the Analytic Distribution Model (prefix-based mapping).
        """
        AnalyticModel = self.env['account.analytic.distribution.model']
        for repair in self:
            repair.analytic_distribution_id = False
            if repair.expense_account_id and repair.expense_account_id.code:
                # Search for matching prefix in Analytic Distribution Model
                dist = AnalyticModel.search(
                    [('account_prefix', '=like',
                      f"{repair.expense_account_id.code}%")],
                    limit=1
                )
                if dist:
                    repair.analytic_distribution_id = dist.analytic_distribution

    # Optional: auto-update analytic account if expense account is manually changed
    @api.onchange('expense_account_id')
    def _onchange_expense_account(self):
        self._compute_analytic_distribution()
