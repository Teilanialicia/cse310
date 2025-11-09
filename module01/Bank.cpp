#include "Account.h"
#include "Bank.h"
#include <string>
#include <vector>

Bank::Bank()
    : account("Teilani", 100)
{

}

void Bank::Withdraw(double amount)
{
    this->account.Withdraw(amount);
}

void Bank::Deposit(double amount)
{
    this->account.Deposit(amount);
}

double Bank::GetBalance()
{
    return this->account.GetBalance();
}
