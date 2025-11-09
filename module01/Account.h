#pragma once
#ifndef ACCOUNT
#include <string>

class Account
{
    private:
    double balance;
    std::string username;

    public:
    Account(std::string username);
    Account(std::string username, double balance);
    void Deposit(double deposit_amount);
    void Withdraw(double withdraw_amount);
    double GetBalance();
};
#endif