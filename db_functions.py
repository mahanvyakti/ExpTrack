import mysql.connector as mysql

def get_initial_queries():
    queries = dict()
    queries['create_budget'] = '''
    CREATE TABLE `budget` (
        `savings` bigint(20) NOT NULL,
        `budget` bigint(20) NOT NULL,
        `date` datetime NOT NULL,
        `username1` varchar(20) NOT NULL
    );
    '''

    queries['create_expense'] = '''
    CREATE TABLE `expense` (
        `category` varchar(20) NOT NULL,
        `mode` varchar(20) NOT NULL,
        `amount` bigint(20) NOT NULL,
        `date` datetime NOT NULL,
        `username` varchar(20) NOT NULL
    );
    '''

    queries['create_income'] = '''
    CREATE TABLE `income` (
        `amount` bigint(20) NOT NULL,
        `date` datetime NOT NULL,
        `source` varchar(30) NOT NULL,
        `username` varchar(20) NOT NULL
    );
    '''

    queries['create_user'] = '''
    CREATE TABLE `user` (
        `username` varchar(20) NOT NULL,
        `password` varchar(20) NOT NULL,
        `name` varchar(20) NOT NULL,
        `age` int(3) NOT NULL,
        `email` varchar(40) NOT NULL,
        `address` text NOT NULL,
        `gender` varchar(10) NOT NULL
    );
    '''

    queries['pk_budget'] = '''
    ALTER TABLE `budget`
        ADD PRIMARY KEY (`date`,`username1`),
        ADD KEY `c3` (`username1`);
    '''

    queries['pk_expense'] = '''
    ALTER TABLE `expense`
        ADD PRIMARY KEY (`date`,`username`),
        ADD KEY `c2` (`username`);
    '''

    queries['pk_income'] = '''
    ALTER TABLE `income`
        ADD PRIMARY KEY (`date`,`username`),
        ADD KEY `c1` (`username`);
    '''

    queries['pk_user'] = '''
    ALTER TABLE `user`
        ADD PRIMARY KEY (`username`);
    '''

    queries['fk_budget_user'] = '''
    ALTER TABLE `budget`
        ADD CONSTRAINT `c3` FOREIGN KEY (`username1`) REFERENCES `user` (`username`);
    '''

    queries['fk_expense_user'] = '''
    ALTER TABLE `expense`
        ADD CONSTRAINT `c2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
    '''

    queries['fk_income_user'] = '''
    ALTER TABLE `income`
        ADD CONSTRAINT `c1` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
    '''

    return queries