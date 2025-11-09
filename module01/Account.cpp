#include <string>
#include "Account.h"

Account::Account(std::string username)
{
    this->balance = 0;
    this->username = username;
}

Account::Account(std::string username, double balance)
{
    this->username = username;
    this->balance = balance;
}

void Account::Deposit(double deposit_amount)
{
    this->balance += deposit_amount;
}

void Account::Withdraw(double withdraw_amount)
{
    this->balance -= withdraw_amount;
}

double Account::GetBalance()
{
    return this->balance;
}