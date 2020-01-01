#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('Database.db')

with con:
    
    cur = con.cursor()
    
    #Create data for the user table
    cur.execute("CREATE TABLE users(UserId INT, UserName TEXT, FullName TEXT, Password TEXT, Picture TEXT, banner TEXT, job TEXT, overview TEXT, exp TEXT, linkedin TEXT)")
    cur.execute("INSERT INTO users VALUES(1,'Admin', 'Glenn ten Cate', '5fcfd41e547a12215b173ff47fdd3739', 'stock.gif', 'banner.png', 'Security Engineer', 'As a coder, hacker, speaker, trainer and security researcher employed at ING Belgium Glenn has over 15 years experience in the field of security. One of the founders of defensive development def[dev]eu a security training and conference series dedicated to helping you build and maintain secure software and also speaking at multiple other security conferences in the world. His goals is to create an open-source software development life cycle with the tools and knowledge gathered over the years.', 'Security tester, Security trainer, Security researcher', 'https://www.linkedin.com/in/glenn-ten-cate')")
    cur.execute("INSERT INTO users VALUES(2,'Moderator', 'Riccardo ten Cate', '0d107d09f5bbe40cade3de5c71e9e9b7', 'meloncat.jpg', 'banner.png', 'Security Engineer', 'As a penetration tester from the Netherlands employed at Zerocopter Riccardo specialises in web-application security and has extensive knowledge in securing web applications in multiple coding languages.', 'Security tester, Security trainer, Security researcher', 'https://www.linkedin.com/in/riccardo-ten-cate-a0b79780')")
    cur.execute("INSERT INTO users VALUES(3,'Test', 'test test', '098f6bcd4621d373cade4e832627b4f6', 'anon.png', 'banner-stock1.jpg', 'Software developer', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tempor aliquam felis, nec condimentum ipsum commodo id. Vivamus sit amet augue nec urna efficitur tincidunt. Vivamus consectetur aliquam lectus commodo viverra. Nunc eu augue nec arcu efficitur faucibus. Aliquam accumsan ac magna convallis bibendum. Quisque laoreet augue eget augue fermentum scelerisque. Vivamus dignissim mollis est dictum blandit. Nam porta auctor neque sed congue. Nullam rutrum eget ex at maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget vestibulum lorem.', 'Software developer, tester', 'https://www.linkedin.com/in/blabla')")
    cur.execute("INSERT INTO users VALUES(4,'John92', 'John Doe', '0cbdc7572ff7d07cc6807a5b102a3b93', 'Aybabtu.png', 'banner-stock2.jpg', 'Chief Information Officer', 'Ipsum dolor sit amet, consectetur adipiscing elit. Quisque tempor aliquam felis, nec condimentum ipsum commodo id. Vivamus sit amet augue nec urna efficitur tincidunt. Vivamus consectetur aliquam lectus commodo viverra. Nunc eu augue nec arcu efficitur faucibus. Aliquam accumsan ac magna convallis bibendum. Quisque laoreet augue eget augue fermentum scelerisque. Vivamus dignissim mollis est dictum blandit', 'Security Policy, Security Controls, Audits', 'https://www.linkedin.com/in/foobar')")

    #Create some data for pageinformation
    cur.execute("CREATE TABLE pages(pageId INT, title TEXT, content TEXT)")
    cur.execute("INSERT INTO pages VALUES(1,'The Dashboard','So, here we are. After a lot of hard work and hassle here we have the dashboard finally up and running. Please take note of this message since it will be updated a lot!')")
    cur.execute("INSERT INTO pages VALUES(2,'Seccond page','Why is there a seccond page, we are going to update the first one right?')")

    con.commit()
    #con.close()
