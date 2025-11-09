#pragma once
#ifndef BANK
#include "Account.h"
#include <string>

class Bank
{
    private:
    Account account;

    public:

    Bank();
    void Withdraw(double amount);
    void Deposit(double amount);
    double GetBalance();
};
#endif