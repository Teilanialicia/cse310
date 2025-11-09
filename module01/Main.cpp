#include <iostream>
#include "Bank.h"

int main() {
    Bank* bank = new Bank();
    double amount;
    char choice;

    bank->Deposit(100);

    while(1)
    {

        std::cout << "\n=============================\n";
        std::cout << "        BANK MENU\n";
        std::cout << "=============================\n";
        std::cout << "1. Check Balance\n";
        std::cout << "2. Deposit\n";
        std::cout << "3. Withdraw\n";
        std::cout << "4. Exit\n";
        std::cout << "-----------------------------\n";
        std::cout << "Enter your choice (1-4): ";
        // This will get the user's input of only ONE character
        std::cin>>choice;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        switch (choice)
        {
        case '1':
            std::cout<<"Your balance is: "<<bank->GetBalance()<<std::endl;
            break;
        
        case '2':
            std::cout<<"How much would you like to deposit?"<<std::endl;
            std::cin>>amount;
            if (std::cin.fail() || amount <= 0)
            {
                std::cin.clear(); // reset error flag
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard bad input
                std::cout << "❌ Invalid amount. Please enter a positive number.\n";
            }
            else
            {
                bank->Deposit(amount);
            }
            break;

        case '3':
            std::cout<<"How much would you like to withdraw?"<<std::endl;
            std::cin>>amount;
            if (std::cin.fail() || amount <= 0)
            {
                std::cin.clear(); // reset error flag
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard bad input
                std::cout << "❌ Invalid amount. Please enter a positive number.\n";
            }
            else
            {
                bank->Withdraw(amount);
            }
            break;

        case '4':
            exit(1);
            break;
        
        default:
            break;
        }
    }

    delete bank;
}