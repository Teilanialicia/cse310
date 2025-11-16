#include "Account.h"
#include "Bank.h"
#include <string>
#include <vector>

Bank::Bank()
    // Instantiates the account property with my name and a starting balance of 100
    : account("Teilani", 100)
{

}

// The method that calls the withdraw method on an account
void Bank::Withdraw(double amount)
{
    this->account.Withdraw(amount);
}

// The method that calls the deposit method on an account
void Bank::Deposit(double amount)
{
    this->account.Deposit(amount);
}

// The method that calls the getBalance method on an account
double Bank::GetBalance()
{
    return this->account.GetBalance();
}
