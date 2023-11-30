truncate table pet_breed RESTART IDENTITY CASCADE;
truncate table pet_pet RESTART IDENTITY CASCADE;
truncate table policy_policy RESTART IDENTITY CASCADE;
truncate table user_user RESTART IDENTITY CASCADE;
truncate table policy_incominginvoice RESTART IDENTITY CASCADE;
truncate table policy_insurancecase RESTART IDENTITY CASCADE;
truncate table policy_serviceprovider RESTART IDENTITY CASCADE;
truncate table user_role RESTART IDENTITY CASCADE;
truncate table tickets_ticket RESTART IDENTITY CASCADE;
truncate table tickets_jobticket RESTART IDENTITY CASCADE;
truncate table tickets_partnerticket RESTART IDENTITY CASCADE;


-- ROLE_TABLE
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'client', 'Role for clients with base permissions');
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'admin', 'Role for staff with super user permissions');
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'provider', 'Role for provider with provider only permissions');


-- USER TABLE
-- INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (true, NULL, 2, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-08-23 00:00:00.000000 +00:00', true, 'petoshield@gmail.com', 'Admin User', true, true, '2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00');

-- BREED_TABLE
-- breed cats
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-03-16 00:00:00.000000 +00:00', '2023-07-21 00:00:00.000000 +00:00', 'Maine Coon', 'cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et eros', 3, 10, 6, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2022-12-28 00:00:00.000000 +00:00', '2023-02-09 00:00:00.000000 +00:00', 'Siamese', 'sit amet cursus id turpis integer aliquet massa id lobortis convallis tortor risus dapibus augue vel accumsan', 2, 20, 8, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-03-16 00:00:00.000000 +00:00', '2023-03-04 00:00:00.000000 +00:00', 'Persian', 'odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit', 3, 18, 9, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-09-05 00:00:00.000000 +00:00', '2023-01-07 00:00:00.000000 +00:00', 'Bengal', 'ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce', 4, 16, 9, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-10-01 00:00:00.000000 +00:00', '2023-05-27 00:00:00.000000 +00:00', 'Sphynx', 'erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit', 5, 15, 4, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-08-31 00:00:00.000000 +00:00', '2023-02-16 00:00:00.000000 +00:00', 'Ragdoll', 'sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit', 6, 16, 2, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2022-12-22 00:00:00.000000 +00:00', '2023-09-17 00:00:00.000000 +00:00', 'British Shorthair', 'eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in', 7, 17, 5, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-02-28 00:00:00.000000 +00:00', '2023-08-26 00:00:00.000000 +00:00', 'Scottish Fold', 'turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum donec', 8, 18, 5, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2022-12-11 00:00:00.000000 +00:00', '2023-04-08 00:00:00.000000 +00:00', 'Abyssinian', 'eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet', 9, 19, 3, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-05-27 00:00:00.000000 +00:00', '2022-11-10 00:00:00.000000 +00:00', 'Norwegian Forest Cat', 'sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque', 10, 20, 4, 'cat');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-05-27 00:00:00.000000 +00:00', '2022-11-10 00:00:00.000000 +00:00', 'Other cat breed', 'other cat breed', 10, 20, 4, 'cat');
-- breed dogs start with id 11
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-07-21 00:00:00.000000 +00:00', '2023-07-03 00:00:00.000000 +00:00', 'Labrador Retriever', 'nunc vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia', 11, 20, 6, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-10-12 00:00:00.000000 +00:00', '2023-01-04 00:00:00.000000 +00:00', 'German Shepherd', 'sed lacus morbi sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel', 12, 20, 5, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-09-17 00:00:00.000000 +00:00', '2023-03-04 00:00:00.000000 +00:00', 'Bulldog', 'tortor duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend', 1, 13, 5, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-09-19 00:00:00.000000 +00:00', '2023-07-09 00:00:00.000000 +00:00', 'Dachshund', 'erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue', 4, 14, 6, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-09-16 00:00:00.000000 +00:00', '2023-01-16 00:00:00.000000 +00:00', 'Poodle', 'duis mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend luctus', 5, 15, 6, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-10-20 00:00:00.000000 +00:00', '2023-09-25 00:00:00.000000 +00:00', 'Siberian Husky', 'vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede', 6, 16, 2, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-08-16 00:00:00.000000 +00:00', '2023-04-05 00:00:00.000000 +00:00', 'Yorkshire Terrier', 'est lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien', 7, 17, 7, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-08-09 00:00:00.000000 +00:00', '2023-07-19 00:00:00.000000 +00:00', 'Rottweiler', 'cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget', 8, 18, 2, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-07-03 00:00:00.000000 +00:00', '2022-11-09 00:00:00.000000 +00:00', 'Chihuahua', 'ac diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est quam pharetra magna ac', 9, 19, 5, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-04-03 00:00:00.000000 +00:00', '2023-09-17 00:00:00.000000 +00:00', 'Boxer', 'dapibus nulla suscipit ligula in lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus', 1, 20, 10, 'dog');
INSERT INTO public.pet_breed (created_at, updated_at, name, description, age_min, age_max, risk_level, species) VALUES ('2023-05-27 00:00:00.000000 +00:00', '2022-11-10 00:00:00.000000 +00:00', 'Other dog breed', 'other cat breed', 10, 20, 4, 'dog');