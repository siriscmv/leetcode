func accountBalanceAfterPurchase(purchaseAmount int) int {
    bal := purchaseAmount % 10
    if bal >= 5 {
        return 100 - purchaseAmount + bal - 10
    } else {
        return 100 - purchaseAmount + bal
    }
}
