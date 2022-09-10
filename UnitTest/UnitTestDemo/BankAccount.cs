using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTestDemo
{
    public class BankAccount
    {

        string _customerName;
        double _balance;

        public BankAccount(string customerName, double balance)
        {
            _customerName = customerName;
            _balance = balance;
        }
        
        public double Balance { get { return _balance; } }

        public void Debit(double amount)
        {
            if (_balance == 0)
                throw new Exception("баланс = 0");
            if (amount <= 0 || amount > _balance)
                throw new ArgumentOutOfRangeException("сумма<=0 or сумма>баланс");
            _balance -= amount;
        }

        public void Credit(double amount)
        {
            if (amount <= 0)
                throw new ArgumentOutOfRangeException("сумма <= 0");
            _balance += amount;
        }
    }
}
