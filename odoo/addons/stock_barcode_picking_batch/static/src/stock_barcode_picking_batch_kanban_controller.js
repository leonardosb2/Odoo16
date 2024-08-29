/** @odoo-module */

import { patch } from 'web.utils';
import { StockBarcodeKanbanController } from '@stock_barcode/kanban/stock_barcode_kanban_controller';

patch(StockBarcodeKanbanController.prototype, 'stock_barcode_picking_batch', {
    /**
     * Add a new batch picking from barcode
     *
     * @private
     * @override
     */
    async createRecord() {
        if (this.props.resModel === 'stock.picking.batch') {
            const action = await this.model.orm.call(
                'stock.picking.batch',
                'open_new_batch_picking',
                [], { context: this.props.context }
            );
            if (action) {
                return this.actionService.doAction(action);
            }
        }
        return this._super(...arguments);
    }
});
