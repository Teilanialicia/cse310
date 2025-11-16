#include <string>
#include "Account.h"

// A constructor that takes only the name of the account holder
Account::Account(std::string username)
{
    this->balance = 0;
    this->username = username;
}

// A constructor that takes the name and starting balance
Account::Account(std::string username, double balance)
{
    this->username = username;
    this->balance = balance;
}

// Deposits the money into the account
void Account::Deposit(double deposit_amount)
{
    this->balance += deposit_amount;
}

// Withdraws the money from the account
void Account::Withdraw(double withdraw_amount)
{
    this->balance -= withdraw_amount;
}

// Returns the current balance of the account
double Account::GetBalance()
{
    return this->balance;
}