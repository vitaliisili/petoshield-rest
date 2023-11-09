truncate table pet_breed RESTART IDENTITY CASCADE;
truncate table pet_pet RESTART IDENTITY CASCADE;
truncate table policy_policy RESTART IDENTITY CASCADE;
truncate table user_user RESTART IDENTITY CASCADE;
truncate table policy_incominginvoice RESTART IDENTITY CASCADE;
truncate table policy_insurancecase RESTART IDENTITY CASCADE;
-- truncate table policy_policy_providers RESTART IDENTITY CASCADE;
truncate table policy_serviceprovider RESTART IDENTITY CASCADE;
truncate table user_role RESTART IDENTITY CASCADE;



-- ROLE_TABLE
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'client', 'Role for clients with base permissions');
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'admin', 'Role for staff with super user permissions');
insert into user_role(created_at, updated_at, name, description) values ('2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00', 'provider', 'Role for provider with provider only permissions');




-- USER_TABLE
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 2, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-08-23 00:00:00.000000 +00:00', true, 'admin@mail.com', 'Admin User', true, true, '2023-09-20 00:00:00.000000 +00:00', '2023-10-14 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-05-24 00:00:00.000000 +00:00', false, 'simple@mail.com', 'Simple User', true, false, '2023-02-06 00:00:00.000000 +00:00', '2023-04-30 00:00:00.000000 +00:00');
--simple users start with id 3
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-05-27 00:00:00.000000 +00:00', false, 'jjoisce0@ameblo.jp', 'Jaymie Joisce', true, false, '2023-02-10 00:00:00.000000 +00:00', '2023-07-17 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-08-26 00:00:00.000000 +00:00', false, 'sarmiger1@youtube.com', 'Sully Armiger', true, false, '2023-09-23 00:00:00.000000 +00:00', '2022-10-29 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-05-09 00:00:00.000000 +00:00', false, 'dastle2@nbcnews.com', 'Danny Astle', true, false, '2023-06-30 00:00:00.000000 +00:00', '2022-12-02 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-10-14 00:00:00.000000 +00:00', false, 'vcrittal3@live.com', 'Vivyanne Crittal', true, false, '2023-05-14 00:00:00.000000 +00:00', '2022-12-05 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-05-10 00:00:00.000000 +00:00', false, 'vpicard4@si.edu', 'Vivyanne Picard', true, false, '2023-08-07 00:00:00.000000 +00:00', '2022-11-03 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-03-17 00:00:00.000000 +00:00', false, 'adurbin5@networksolutions.com', 'Arlina Durbin', true, false, '2023-03-20 00:00:00.000000 +00:00', '2022-11-21 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-01-13 00:00:00.000000 +00:00', false, 'avedyasov6@lycos.com', 'Augustus Vedyasov', true, false, '2023-08-31 00:00:00.000000 +00:00', '2023-07-30 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-01-24 00:00:00.000000 +00:00', false, 'bsackett7@scribd.com', 'Birgitta Sackett', true, false, '2023-01-28 00:00:00.000000 +00:00', '2023-07-02 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-08-05 00:00:00.000000 +00:00', false, 'gmougel8@e-recht24.de', 'Gwynne Mougel', true, false, '2022-11-06 00:00:00.000000 +00:00', '2023-06-08 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2022-11-11 00:00:00.000000 +00:00', false, 'hgebbe9@cyberchimps.com', 'Hermia Gebbe', true, false, '2023-10-10 00:00:00.000000 +00:00', '2023-09-02 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-10-15 00:00:00.000000 +00:00', false, 'yculmera@wix.com', 'Yard Culmer', true, false, '2023-09-26 00:00:00.000000 +00:00', '2023-09-02 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2022-12-27 00:00:00.000000 +00:00', false, 'ebecerrab@tripod.com', 'Edita Becerra', true, false, '2023-07-22 00:00:00.000000 +00:00', '2023-02-14 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-09-15 00:00:00.000000 +00:00', false, 'aswainsc@nbcnews.com', 'Aloysius Swains', true, false, '2022-12-01 00:00:00.000000 +00:00', '2023-08-14 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2022-12-31 00:00:00.000000 +00:00', false, 'fcordled@answers.com', 'Florry Cordle', true, false, '2023-05-09 00:00:00.000000 +00:00', '2023-05-28 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-06-14 00:00:00.000000 +00:00', false, 'schmiele@mit.edu', 'Sarita Chmiel', true, false, '2023-06-11 00:00:00.000000 +00:00', '2023-01-30 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-05-11 00:00:00.000000 +00:00', false, 'ilennoxf@princeton.edu', 'Iona Lennox', true, false, '2023-04-19 00:00:00.000000 +00:00', '2023-07-28 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-08-27 00:00:00.000000 +00:00', false, 'nschruyerg@archive.org', 'Nani Schruyer', true, false, '2022-11-20 00:00:00.000000 +00:00', '2023-01-05 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'aprandyh@wufoo.com', 'Arden Prandy', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'aprandasd@wufoo.com', 'Arden Goren', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (is_verified, image, role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (false, NULL, 1, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'aasd@wufoo.com', 'Lily Soren', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
-- provider users start with id 23
INSERT INTO public.user_user (role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (3, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'provider1@mail.com', 'Sasha Olimp', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (3, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'provider2@mail.com', 'Cara Morex', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (3, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'provider3@mail.com', 'Loren Dalos', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (3, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'provider4@mail.com', 'Iros Gamer', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');
INSERT INTO public.user_user (role_id, password, last_login, is_superuser, email, name, is_active, is_staff, created_at, updated_at) VALUES (3, 'pbkdf2_sha256$600000$NxtDXwYFo349VfKTw1lQJN$ywdRommTzYnkiQWbk1oCwJqSh8gESadpWzlIi0tBmrU=', '2023-04-16 00:00:00.000000 +00:00', false, 'provider5@mail.com', 'Mira Golem', true, false, '2023-06-19 00:00:00.000000 +00:00', '2022-12-20 00:00:00.000000 +00:00');




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




-- PET_TABLE
-- pets cats
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-01-15 00:00:00.000000 +00:00', '2023-04-14 00:00:00.000000 +00:00', 'Haze', 14, 'M', 'cat', 1, 3);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-01-18 00:00:00.000000 +00:00', '2023-08-08 00:00:00.000000 +00:00', 'Cassie', 6, 'M', 'cat', 1, 4);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-09-29 00:00:00.000000 +00:00', '2023-01-14 00:00:00.000000 +00:00', 'Lauri', 2, 'F', 'cat', 1, 4);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-04 00:00:00.000000 +00:00', '2023-08-05 00:00:00.000000 +00:00', 'Skye', 15, 'M', 'cat', 2, 5);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-09-05 00:00:00.000000 +00:00', '2023-10-17 00:00:00.000000 +00:00', 'Marni', 20, 'F', 'cat', 2, 6);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-03-10 00:00:00.000000 +00:00', '2023-07-26 00:00:00.000000 +00:00', 'Patin', 3, 'M', 'cat', 3, 7);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-04-08 00:00:00.000000 +00:00', '2023-05-15 00:00:00.000000 +00:00', 'Darrelle', 18, 'F', 'cat', 4, 8);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-02-10 00:00:00.000000 +00:00', '2023-09-06 00:00:00.000000 +00:00', 'Marylee', 5, 'F', 'cat', 5, 8);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-07-26 00:00:00.000000 +00:00', '2023-03-26 00:00:00.000000 +00:00', 'Jordain', 3, 'F', 'cat', 6, 10);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-03-23 00:00:00.000000 +00:00', '2023-04-07 00:00:00.000000 +00:00', 'Annabell', 10, 'F', 'cat', 7, 11);
-- pets dogs start with id 11
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-09-25 00:00:00.000000 +00:00', '2023-06-09 00:00:00.000000 +00:00', 'Bennett', 11, 'M', 'dog', 10, 12);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-04-04 00:00:00.000000 +00:00', '2023-06-15 00:00:00.000000 +00:00', 'Valentin', 13, 'M', 'dog', 10, 13);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-10-10 00:00:00.000000 +00:00', '2023-07-06 00:00:00.000000 +00:00', 'Rebekkah', 2, 'F', 'dog', 10, 14);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-01-16 00:00:00.000000 +00:00', '2023-01-15 00:00:00.000000 +00:00', 'Merrielle', 10, 'F', 'dog', 11, 15);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-04-27 00:00:00.000000 +00:00', '2023-03-17 00:00:00.000000 +00:00', 'Paola', 14, 'F', 'dog', 11, 16);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-07-30 00:00:00.000000 +00:00', '2023-03-15 00:00:00.000000 +00:00', 'Laurel', 17, 'F', 'dog', 12, 17);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-09-28 00:00:00.000000 +00:00', '2022-12-02 00:00:00.000000 +00:00', 'Gerome', 19, 'M', 'dog', 13, 18);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2023-08-28 00:00:00.000000 +00:00', '2023-03-10 00:00:00.000000 +00:00', 'Donovan', 12, 'M', 'dog', 14, 19);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-02 00:00:00.000000 +00:00', '2023-07-02 00:00:00.000000 +00:00', 'Joycelin', 5, 'F', 'dog', 15, 20);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-22 00:00:00.000000 +00:00', '2022-10-31 00:00:00.000000 +00:00', 'Brandy', 15, 'M', 'dog', 16, 20);
-- pets for simple user with id 21, 22, 23
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-22 00:00:00.000000 +00:00', '2022-10-31 00:00:00.000000 +00:00', 'Margo', 15, 'F', 'cat', 1, 2);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-22 00:00:00.000000 +00:00', '2022-10-31 00:00:00.000000 +00:00', 'Briko', 15, 'M', 'dog', 11, 2);
INSERT INTO public.pet_pet (created_at, updated_at, name, age, gender, species, breed_id, user_id) VALUES ('2022-11-22 00:00:00.000000 +00:00', '2022-10-31 00:00:00.000000 +00:00', 'Lamer', 15, 'M', 'dog', 12, 2);




-- POLICY_TABLE
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (11.25, '2023-06-11 00:00:00.000000 +0200', '2023-06-11 00:00:00.000000 +0200', '84-121-4860', '2023-06-11', '2023-01-08', 'active', 10000.00, 10000.00, 250.00, 1);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (15.50, '2023-01-03 00:00:00.000000 +0200', '2023-01-03 00:00:00.000000 +0200', '19-785-5157', '2023-01-03', '2023-05-30', 'active', 10000.00, 10000.00, 250.00, 2);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (11.21, '2022-11-27 00:00:00.000000 +0200', '2022-11-27 00:00:00.000000 +0200', '88-419-1628', '2022-11-27', '2023-01-03', 'active', 10000.00, 10000.00, 250.00, 3);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (16.47, '2023-03-31 00:00:00.000000 +0200', '2023-03-31 00:00:00.000000 +0200', '54-352-9173', '2023-03-31', '2023-06-09', 'active', 10000.00, 10000.00, 250.00, 4);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (13.99, '2023-07-26 00:00:00.000000 +0200', '2023-07-26 00:00:00.000000 +0200', '18-965-0653', '2023-07-26', '2023-07-20', 'active', 10000.00, 10000.00, 250.00, 5);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (10.48, '2023-03-19 00:00:00.000000 +0200', '2023-03-19 00:00:00.000000 +0200', '23-175-8279', '2023-03-19', '2023-03-24', 'active', 10000.00, 10000.00, 250.00, 6);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (19.75, '2023-03-31 00:00:00.000000 +0200', '2023-03-31 00:00:00.000000 +0200', '78-974-5259', '2023-03-31', '2023-09-19', 'active', 10000.00, 10000.00, 250.00, 7);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (13.50, '2023-02-14 00:00:00.000000 +0200', '2023-02-14 00:00:00.000000 +0200', '97-366-2381', '2023-02-14', '2023-05-13', 'active', 10000.00, 10000.00, 250.00, 8);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (16.45, '2023-07-04 00:00:00.000000 +0200', '2023-07-04 00:00:00.000000 +0200', '22-546-9647', '2023-07-04', '2022-11-17', 'invalid', 10000.00, 10000.00, 250.00, 9);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (12.10, '2023-05-19 00:00:00.000000 +0200', '2023-05-19 00:00:00.000000 +0200', '87-456-7934', '2023-05-19', '2022-11-30', 'invalid', 10000.00, 10000.00, 250.00, 10);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (11.20, '2023-10-10 00:00:00.000000 +0200', '2023-10-10 00:00:00.000000 +0200', '23-144-6524', '2023-10-10', '2023-09-25', 'invalid', 10000.00, 10000.00, 250.00, 11);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (16.39, '2023-04-20 00:00:00.000000 +0200', '2023-04-20 00:00:00.000000 +0200', '34-744-7222', '2023-04-20', '2023-08-20', 'invalid', 10000.00, 10000.00, 250.00, 12);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (11.29, '2023-09-04 00:00:00.000000 +0200', '2023-09-04 00:00:00.000000 +0200', '88-674-2736', '2023-09-04', '2023-02-26', 'invalid', 10000.00, 10000.00, 250.00, 13);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (16.85, '2023-03-19 00:00:00.000000 +0200', '2023-03-19 00:00:00.000000 +0200', '71-272-4331', '2023-03-19', '2023-03-27', 'invalid', 10000.00, 10000.00, 250.00, 14);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (13.40, '2022-11-24 00:00:00.000000 +0200', '2022-11-24 00:00:00.000000 +0200', '26-150-5465', '2022-11-24', '2023-04-06', 'invalid', 10000.00, 10000.00, 250.00, 15);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (11.99, '2022-11-04 00:00:00.000000 +0200', '2022-11-04 00:00:00.000000 +0200', '59-159-6495', '2022-11-04', '2022-12-26', 'invalid', 10000.00, 10000.00, 250.00, 16);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (18.87, '2022-11-29 00:00:00.000000 +0200', '2022-11-29 00:00:00.000000 +0200', '65-431-4428', '2022-11-29', '2023-06-28', 'expired', 10000.00, 10000.00, 250.00, 17);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (10.55, '2023-09-26 00:00:00.000000 +0200', '2023-09-26 00:00:00.000000 +0200', '49-053-5404', '2023-09-26', '2023-07-22', 'expired', 10000.00, 10000.00, 250.00, 18);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (13.45, '2022-11-01 00:00:00.000000 +0200', '2022-11-01 00:00:00.000000 +0200', '35-544-9388', '2022-11-01', '2023-06-20', 'expired', 10000.00, 10000.00, 250.00, 19);
INSERT INTO public.policy_policy (price, created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES (17.60, '2023-10-12 00:00:00.000000 +0200', '2023-10-12 00:00:00.000000 +0200', '32-128-1016', '2023-10-12', '2022-12-11', 'expired', 10000.00, 10000.00, 250.00, 20);
-- policy for simple user pets with id 21, 22, 23
INSERT INTO public.policy_policy (created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES ('2023-10-12 00:00:00.000000 +0200', '2023-10-12 00:00:00.000000 +0200', '34-227-2019', '2023-10-12', '2022-12-11', 'active', 10000.00, 10000.00, 250.00, 21);
INSERT INTO public.policy_policy (created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES ('2023-10-12 00:00:00.000000 +0200', '2023-10-12 00:00:00.000000 +0200', '35-323-3026', '2023-10-12', '2022-12-11', 'invalid', 10000.00, 10000.00, 250.00, 22);
INSERT INTO public.policy_policy (created_at, updated_at, policy_number, start_date, end_date, status, initial_limit, current_limit, deductible, pet_id) VALUES ('2023-10-12 00:00:00.000000 +0200', '2023-10-12 00:00:00.000000 +0200', '36-425-4013', '2023-10-12', '2022-12-11', 'expired', 10000.00, 10000.00, 250.00, 23);





-- SERVICE_PROVIDER_TABLE
INSERT INTO public.policy_serviceprovider (user_id, created_at, updated_at, company_name, phone, registration_number, address, iban) VALUES (23, '2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000 +00:00', 'Breitenberg-Bashirian', '257-665-9176', '69-602-9552', 'Suite 35', 'EE59 5774 7361 0463 0291');
INSERT INTO public.policy_serviceprovider (user_id, created_at, updated_at, company_name, phone, registration_number, address, iban) VALUES (24, '2023-01-19 00:00:00.000000 +00:00', '2023-02-01 00:00:00.000000 +00:00', 'Langworth and Sons', '819-435-2830', '56-986-8666', '1st Floor', 'ME26 6553 5538 6490 0821 86');
INSERT INTO public.policy_serviceprovider (user_id, created_at, updated_at, company_name, phone, registration_number, address, iban) VALUES (25, '2023-01-20 00:00:00.000000 +00:00', '2022-10-26 00:00:00.000000 +00:00', 'Kub-Donnelly', '426-438-8610', '80-472-9169', 'Room 154', 'BR95 8978 2553 6038 2773 7375 4');
INSERT INTO public.policy_serviceprovider (user_id, created_at, updated_at, company_name, phone, registration_number, address, iban) VALUES (26, '2023-08-22 00:00:00.000000 +00:00', '2023-05-29 00:00:00.000000 +00:00', 'Wehner-Dickens', '166-249-6763', '42-961-3936', 'Suite 26', 'PK20 GAMB KSRA 6GY1 ABUU RFQE');
INSERT INTO public.policy_serviceprovider (user_id, created_at, updated_at, company_name, phone, registration_number, address, iban) VALUES (27, '2023-07-05 00:00:00.000000 +00:00', '2023-01-03 00:00:00.000000 +00:00', 'Cole, Wolf and Jacobs', '873-198-5877', '91-303-5588', 'PO Box 18858', 'LV16 ROLV JWKU GEWB YGPS Z');




-- POLICY__PROVIDER_RELATION_TABLE
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (1, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (2, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (3, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (4, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (5, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (6, 2);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (7, 2);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (8, 2);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (9, 2);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (10, 3);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (11, 3);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (12, 3);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (13, 4);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (14, 4);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (15, 5);
-- -- policy relation for simple user policies
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (21, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (22, 1);
-- INSERT INTO public.policy_policy_providers (policy_id, serviceprovider_id) VALUES (23, 2);




-- INSURANCE_CASES_TABLE
-- service provider with id 1
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 1, 1, 'accept',  'case 1 description');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 2, 1, 'accept',  'case 2 description');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 3, 1, 'process', 'case 3 description');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 4, 1, 'reject',  'case 3 description');
-- service provider with id 2
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 5, 2, 'accept',  'case 4 description');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 6, 2, 'accept',  'case 5 description');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 7, 2, 'reject',  'case 6 description');
-- service provider with id 3
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 8, 3, 'accept',  'case 7 description');
-- insurance case for simple users pets
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 21, 1, 'accept',  'case 1 for simple user pets');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 21, 2, 'accept',  'case 2 for simple user pets');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 22, 3, 'process', 'case 3 for simple user pets');
INSERT INTO policy_insurancecase(created_at, updated_at, claim_date, policy_id, service_provider_id, status, description) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', '2022-12-20 00:00:00.000000 +00:00', 23, 4, 'reject',  'case 4 for simple user pets');





-- INSURANCE_INCOMING_INVOICES_TABLE
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 1,  200.00,  '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 2,  250.00,  '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 3,  150.00,  '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 4,  123.33,  '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 5,  1231.65, '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 6,  49.12,   '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 7,  100.00,  '2023-10-19 00:00:00.000000');
--invoice for simple user pets
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 9,  234.18,  '2023-10-19 00:00:00.000000');
INSERT INTO policy_incominginvoice(created_at, updated_at, insurance_case_id, amount, invoice_date) VALUES ('2022-12-20 00:00:00.000000 +00:00', '2023-10-19 00:00:00.000000', 10,  654.43,  '2023-10-19 00:00:00.000000');
