truncate table pet_breed RESTART IDENTITY CASCADE;
truncate table pet_pet RESTART IDENTITY CASCADE;
truncate table policy_policy RESTART IDENTITY CASCADE;
truncate table user_user RESTART IDENTITY CASCADE;

-- USER_TABLE

insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (true, true, true, 'Admin User', 'admin@mail.com', 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '8/23/2023', '9/20/2023', '10/14/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Simple User', 'simple@mail.com', 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '5/24/2023', '2/6/2023', '4/30/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Jaymie Joisce', 'jjoisce0@ameblo.jp', '$2a$04$oEMmPwjI4DSGC7rwB7SnrOXCj7ph0v2Ban1xwjxy23ifPiDIDOrtS', '5/27/2023', '2/10/2023', '7/17/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Sully Armiger', 'sarmiger1@youtube.com', '$2a$04$QilfslJNfHah6qBZBEECDOawo8VDsKmFHUr2KmjejO5wXoWJPB8E.', '8/26/2023', '9/23/2023', '10/29/2022');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Danny Astle', 'dastle2@nbcnews.com', '$2a$04$k7bebtLdSiStAUt63zh45eQbguspJCgqWPbk9f0qHKp.5DCf45TkC', '5/9/2023', '6/30/2023', '12/2/2022');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Vivyanne Crittal', 'vcrittal3@live.com', '$2a$04$Dg3FbdcoFjL/UE.MGBYDGOEAxHLGbxtCbBwfFdAL3JbjyYdsEUL6i', '10/14/2023', '5/14/2023', '12/5/2022');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Vivyanne Picard', 'vpicard4@si.edu', '$2a$04$z8LYF3alv0CroxlwUboOfOc0Glq/6qy4Vq2k.9JYy.Dwx3UQ0a/P2', '5/10/2023', '8/7/2023', '11/3/2022');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Arlina Durbin', 'adurbin5@networksolutions.com', '$2a$04$BM26EaYAvTldmi8dcirISOIQv4hPijuvDp9aORN/6MqlCS3cte0Ia', '3/17/2023', '3/20/2023', '11/21/2022');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Augustus Vedyasov', 'avedyasov6@lycos.com', '$2a$04$VnzUghwiI2JdMyBNC.nMtuL9MPir8CX8e.EpoqQLvoG7loFweOKwS', '1/13/2023', '8/31/2023', '7/30/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Birgitta Sackett', 'bsackett7@scribd.com', '$2a$04$3LtKyx1ZMjG7HvOQDd5q7.cpHKBtrn62sFaoFCS0kOGTNoUwsxVny', '1/24/2023', '1/28/2023', '7/2/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Gwynne Mougel', 'gmougel8@e-recht24.de', '$2a$04$0kLMpaCkqUdGGb0or.0SHeYi37KG4Nik1cI.vJ50uizBfavILBuby', '8/5/2023', '11/6/2022', '6/8/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Hermia Gebbe', 'hgebbe9@cyberchimps.com', '$2a$04$ElN.Styc0u/yOZ3t6Pf/YeAQCd5OW6N2Kfz5rqIW2hXEpXB8FjqWS', '11/11/2022', '10/10/2023', '9/2/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Yard Culmer', 'yculmera@wix.com', '$2a$04$rH4f5Amn/xzVOj0aBm.N3eFxE/TF/jzbYvY7NxyQYjeZBfZd95yvi', '10/15/2023', '9/26/2023', '9/2/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Edita Becerra', 'ebecerrab@tripod.com', '$2a$04$4iBKvgXJwzavU0eYpGIRNOo30QoJriCMs9Awjhn0eVg4iAFORnyci', '12/27/2022', '7/22/2023', '2/14/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Aloysius Swains', 'aswainsc@nbcnews.com', '$2a$04$SXzrPHppTGg/WE9MCkuJqeIXa1RL0/5xufd3zEPLDCCUOLy0k8DeC', '9/15/2023', '12/1/2022', '8/14/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Florry Cordle', 'fcordled@answers.com', '$2a$04$i41aPARFTzbBJO9So114QuzTSIeWLyTbzlcokefdeAy4vHUy01z9e', '12/31/2022', '5/9/2023', '5/28/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Sarita Chmiel', 'schmiele@mit.edu', '$2a$04$5r1fXAhpQwDX2nz84BTZWeEarBMYY5w5JHFumC7nQ5zpIrD1hjjEa', '6/14/2023', '6/11/2023', '1/30/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Iona Lennox', 'ilennoxf@princeton.edu', '$2a$04$d2rlgcp/xQLuJMoGVEf9CujUEvi3SBFhlcGJ0Vtu5WZIBI8o2kOy.', '5/11/2023', '4/19/2023', '7/28/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Nani Schruyer', 'nschruyerg@archive.org', '$2a$04$gMEFU2T3zvIIsWwChn0AEenBd8C5Gad7MzwieqoFu6mk2w34a5sFO', '8/27/2023', '11/20/2022', '1/5/2023');
insert into user_user (is_staff, is_superuser, is_active, name, email, password, last_login, created_at, updated_at) values (false, false, true, 'Arden Prandy', 'aprandyh@wufoo.com', '$2a$04$WC9O2EY1SdBe6qoH6riUWOJ6oGo5WSVBIiS9i176OmFq.M7tGvSry', '4/16/2023', '6/19/2023', '12/20/2022');

-- BREED_TABLE
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 1, 1, 'Snycerus caffer', 6, 'cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et eros', '7/21/2023', '3/16/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 2, 2, 'Lamprotornis nitens', 8, 'sit amet cursus id turpis integer aliquet massa id lobortis convallis tortor risus dapibus augue vel accumsan', '2/9/2023', '12/28/2022');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 3, 3, 'Phascogale calura', 9, 'odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit', '3/4/2023', '3/16/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 4, 4, 'Nycticorax nycticorax', 9, 'ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce', '1/7/2023', '9/5/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 5, 5, 'Anthropoides paradisea', 4, 'erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit', '5/27/2023', '10/1/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 6, 6, 'Spilogale gracilis', 2, 'sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit', '2/16/2023', '8/31/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 7, 7, 'Tayassu pecari', 5, 'eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in', '9/17/2023', '12/22/2022');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 8, 8, 'Terrapene carolina', 5, 'turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec', '8/26/2023', '2/28/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 9, 9, 'Thalasseus maximus', 3, 'eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet', '4/8/2023', '12/11/2022');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 10, 10, 'Cervus elaphus', 4, 'sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque', '11/10/2022', '5/27/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('cat', 11, 11, 'unavailable', 6, 'nunc vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia', '7/3/2023', '7/21/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 12, 12, 'Colaptes campestroides', 5, 'sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel', '1/4/2023', '10/12/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 13, 13, 'Notechis semmiannulatus', 5, 'tortor duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend', '3/4/2023', '9/17/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 14, 14, 'Ictalurus furcatus', 6, 'erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue', '7/9/2023', '9/19/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 15, 15, 'Recurvirostra avosetta', 6, 'duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend luctus', '1/16/2023', '9/16/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 16, 16, 'Papio cynocephalus', 2, 'vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede', '9/25/2023', '10/20/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 17, 17, 'Geochelone radiata', 7, 'est lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien', '4/5/2023', '8/16/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 18, 18, 'Rangifer tarandus', 2, 'cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget', '7/19/2023', '8/9/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 19, 19, 'Ciconia ciconia', 5, 'ac diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est quam pharetra magna ac', '11/9/2022', '7/3/2023');
insert into pet_breed (species, age_min, age_max, name, risk_level, description, updated_at, created_at) values ('dog', 20, 20, 'Semnopithecus entellus', 10, 'dapibus nulla suscipit ligula in lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus', '9/17/2023', '4/3/2023');

-- PET_TABLE
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 14, 'Haze', '4/14/2023', '1/15/2023', 'M', 13, 15);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 6, 'Cassie', '8/8/2023', '1/18/2023', 'M', 14, 20);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 2, 'Lauri', '1/14/2023', '9/29/2023', 'F', 12, 10);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 15, 'Skye', '8/5/2023', '11/4/2022', 'M', 12, 4);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 20, 'Marni', '10/17/2023', '9/5/2023', 'F', 20, 13);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 3, 'Patin', '7/26/2023', '3/10/2023', 'M', 7, 19);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 18, 'Darrelle', '5/15/2023', '4/8/2023', 'F', 12, 5);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 5, 'Marylee', '9/6/2023', '2/10/2023', 'F', 2, 7);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('cat', 3, 'Jordain', '3/26/2023', '7/26/2023', 'F', 16, 16);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 10, 'Annabell', '4/7/2023', '3/23/2023', 'F', 6, 11);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 11, 'Bennett', '6/9/2023', '9/25/2023', 'M', 9, 14);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 13, 'Valentin', '6/15/2023', '4/4/2023', 'M', 19, 5);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 2, 'Rebekkah', '7/6/2023', '10/10/2023', 'F', 14, 7);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 10, 'Merrielle', '1/15/2023', '1/16/2023', 'F', 3, 3);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 14, 'Paola', '3/17/2023', '4/27/2023', 'F', 18, 11);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 17, 'Laurel', '3/15/2023', '7/30/2023', 'F', 11, 6);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 19, 'Gerome', '12/2/2022', '9/28/2023', 'M', 7, 12);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 12, 'Donovan', '3/10/2023', '8/28/2023', 'M', 1, 4);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 5, 'Joycelin', '7/2/2023', '11/2/2022', 'F', 17, 10);
insert into pet_pet (species, age, name, updated_at, created_at, gender, breed_id, user_id) values ('dog', 15, 'Brandy', '10/31/2022', '11/22/2022', 'M', 18, 8);

-- POLICY_TABLE
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 20, '6/11/2023', '1/8/2023', '11/5/2022', '7/19/2023', '84-121-4860');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 10, '1/3/2023', '5/30/2023', '4/10/2023', '10/2/2023', '19-785-5157');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 17, '11/27/2022', '1/3/2023', '11/25/2022', '3/16/2023', '88-419-1628');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 2, '3/31/2023', '6/9/2023', '4/11/2023', '9/30/2023', '54-352-9173');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 15, '7/26/2023', '7/20/2023', '8/7/2023', '4/17/2023', '18-965-0653');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 8, '3/19/2023', '3/24/2023', '7/28/2023', '10/16/2023', '23-175-8279');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 14, '3/31/2023', '9/19/2023', '6/4/2023', '7/9/2023', '78-974-5259');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'active', 10, '2/14/2023', '5/13/2023', '7/31/2023', '3/27/2023', '97-366-2381');
-- invalid policies
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 7, '7/4/2023', '11/17/2022', '3/14/2023', '3/7/2023', '22-546-9647');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 16, '5/19/2023', '11/30/2022', '5/27/2023', '9/28/2023', '87-456-7934');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 5, '10/10/2023', '9/25/2023', '2/17/2023', '2/20/2023', '23-144-6524');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 17, '4/20/2023', '8/20/2023', '12/10/2022', '7/1/2023', '34-744-7222');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 16, '9/4/2023', '2/26/2023', '5/10/2023', '3/14/2023', '88-674-2736');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 14, '3/19/2023', '3/27/2023', '2/25/2023', '10/26/2022', '71-272-4331');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 8, '11/24/2022', '4/6/2023', '6/27/2023', '6/6/2023', '26-150-5465');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'invalid', 11, '11/4/2022', '12/26/2022', '2/14/2023', '8/3/2023', '59-159-6495');
-- expired policies
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'expired', 3, '11/29/2022', '6/28/2023', '9/13/2023', '7/23/2023', '65-431-4428');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'expired', 14, '9/26/2023', '7/22/2023', '10/14/2023', '10/23/2023', '49-053-5404');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'expired', 16, '11/1/2022', '6/20/2023', '7/29/2023', '2/5/2023', '35-544-9388');
insert into policy_policy (initial_limit, current_limit, deductible, status, pet_id, start_date, end_date, updated_at, created_at, policy_number) values (10000, 10000, 250, 'expired', 14, '10/12/2023', '12/11/2022', '2/4/2023', '3/23/2023', '32-128-1016');

-- SERVICE_PROVIDER_TABLE
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Breitenberg-Bashirian', '69-602-9552', 'ltatnell0@qq.com', '257-665-9176', 'Suite 35', 'EE59 5774 7361 0463 0291', '12/20/2022', '10/19/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Langworth and Sons', '56-986-8666', 'mlavigne1@engadget.com', '819-435-2830', '1st Floor', 'ME26 6553 5538 6490 0821 86', '1/19/2023', '2/1/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Kub-Donnelly', '80-472-9169', 'cstiling2@parallels.com', '426-438-8610', 'Room 154', 'BR95 8978 2553 6038 2773 7375 4', '1/20/2023', '10/26/2022');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Wehner-Dickens', '42-961-3936', 'acasari3@twitter.com', '166-249-6763', 'Suite 26', 'PK20 GAMB KSRA 6GY1 ABUU RFQE', '8/22/2023', '5/29/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Cole, Wolf and Jacobs', '91-303-5588', 'wcampsall4@istockphoto.com', '873-198-5877', 'PO Box 18858', 'LV16 ROLV JWKU GEWB YGPS Z', '7/5/2023', '1/3/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Hirthe, Larson and Schuster', '21-580-5096', 'dletten5@dagondesign.com', '834-439-5617', '13th Floor', 'MT73 RNTH 4683 03RE RHEP JB1F JJT', '4/6/2023', '9/2/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Metz, Goldner and Beer', '70-918-4301', 'dcliss6@ebay.com', '385-951-5747', '17th Floor', 'AD66 0120 4357 U9OT RDZJ KOG7', '1/21/2023', '10/5/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Huels and Sons', '18-036-2787', 'cingilson7@exblog.jp', '623-272-6243', 'Room 1770', 'SK61 3323 9709 4487 0815 1247', '3/1/2023', '7/9/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Hackett, Jenkins and Kassulke', '51-829-9942', 'nhowis8@networkadvertising.org', '314-275-3255', '8th Floor', 'BH48 FYPK MRWZ HVQB 1RYI 1R', '12/5/2022', '5/17/2023');
insert into policy_serviceprovider (company_name, registration_number, email, phone, address, iban, created_at, updated_at) values ('Schumm, Moore and Hessel', '97-348-7547', 'zhoulworth9@dell.com', '556-327-3152', 'Room 398', 'HU85 5799 2754 7723 5325 2604', '12/8/2022', '2/7/2023');

-- POLICY__PROVIDER_RELATION_TABLE
insert into policy_policy_providers(policy_id, serviceprovider_id) values (1, 1);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (1, 2);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (2, 3);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (3, 4);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (4, 5);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (5, 5);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (5, 6);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (5, 7);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (6, 1);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (7, 8);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (8, 8);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (9, 9);
insert into policy_policy_providers(policy_id, serviceprovider_id) values (10, 10);