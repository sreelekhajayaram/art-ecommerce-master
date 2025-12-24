# TODO: Prevent Order Placement When Stock is 0

## Tasks
- [x] Update product_detail.html: Show "Out of Stock" if product.stock == 0 instead of add to cart form.
- [x] Modify add_to_cart view: Add stock check before adding to cart.
- [ ] Update checkout view: Check stock before allowing checkout.
- [ ] Update payment_portal view: Check stock before allowing payment.

## Notes
- Ensure users cannot add out-of-stock items to cart.
- Prevent checkout if any item in cart has insufficient stock.
