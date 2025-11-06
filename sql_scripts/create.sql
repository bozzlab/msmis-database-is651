START TRANSACTION;

-- ------------------
-- 1. Create ENUM Types
-- ------------------

CREATE TYPE gender_enum AS ENUM ('F', 'M', 'Others','Rather not to say');
CREATE TYPE subscription_plan_billing_cycle AS ENUM ('MONTHLY', 'YEARLY', 'QUARTERLY', 'HALF_YEAR');
CREATE TYPE user_subscriptions_status AS ENUM ('ACTIVE', 'CANCELLED', 'TRIAL', 'PAST_DUE', 'EXPIRED');
CREATE TYPE user_notification_status_enum AS ENUM ('PENDING', 'SENT', 'READ', 'FAILED');
CREATE TYPE notification_type_channel_enum AS ENUM ('EMAIL', 'APP_PUSH', 'SMS');
CREATE TYPE goal_target_enum AS ENUM ('LIMIT EXPENSE', 'SAVING');
CREATE TYPE goal_status_enum AS ENUM ('IN_PROGRESS', 'FAILED', 'PENDING', 'SUCCESS');
CREATE TYPE income_interval_enum AS ENUM ('WEEKLY', 'MONTHLY', 'BI_WEEKLY', 'QUARTERLY', 'HALF_YEAR','YEARLY');
CREATE TYPE file_type_enum AS ENUM ('jpg', 'png', 'pdf');
CREATE TYPE expense_interval_enum AS ENUM ('WEEKLY', 'MONTHLY', 'BI_WEEKLY', 'QUARTERLY', 'HALF_YEAR','YEARLY');

-- ------------------
-- 2. Create Trigger Function for last_modified_at
-- ------------------

CREATE OR REPLACE FUNCTION update_last_modified_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_modified_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';


-- ------------------
-- 3. Create Tables
-- ------------------

-- Reference Tables
CREATE TABLE occupations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE work_experience_levels (
  id SERIAL PRIMARY KEY,
  level VARCHAR(255),
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE postal_codes (
  id SERIAL PRIMARY KEY,
  postal_code VARCHAR(20) UNIQUE NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE education_levels (
  id SERIAL PRIMARY KEY,
  level VARCHAR(255),
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE currencies (
  id SERIAL PRIMARY KEY,
  code VARCHAR(10) UNIQUE NOT NULL,
  name VARCHAR(100),
  active BOOLEAN DEFAULT TRUE,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE partners (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE partner_products (
  id SERIAL PRIMARY KEY,
  partner_id INT NOT NULL,
  type VARCHAR(100),
  remark TEXT,
  is_active BOOLEAN DEFAULT TRUE,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User Tables
CREATE TABLE users (
 id serial NOT NULL,
    username character varying(255) NOT NULL,
    password_hash character varying(255) NOT NULL,
    phone_number character varying(50) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    email character varying(255) NOT NULL,
    dob date NOT NULL,
    gender gender_enum NOT NULL,
    occupation_id integer NOT NULL,
    work_experience_level_id integer NOT NULL,
    education_level_id integer NOT NULL,
    postal_code_id integer NOT NULL,
    currency_id integer NOT NULL,
    personal_data_consent boolean NOT NULL,
    marketing_consent boolean NOT NULL,
    last_modified_at timestamp without time zone NULL DEFAULT CURRENT_TIMESTAMP,
    created_at timestamp without time zone NULL DEFAULT CURRENT_TIMESTAMP,
    age integer NOT NULL DEFAULT (
      (
        (2025)::numeric - EXTRACT(
          year
          FROM
            dob
        )
      )
    )::integer
  );

CREATE TABLE subscription_plans (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL UNIQUE,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    billing_cycle subscription_plan_billing_cycle NOT NULL, 
    features JSONB,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_subscriptions (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL UNIQUE,
  plan_id INT NOT NULL,
  status  user_subscriptions_status NOT NULL,
  renews_automatically BOOLEAN NOT NULL DEFAULT TRUE,
  last_payment_date TIMESTAMP WITH TIME ZONE,
  next_billing_date TIMESTAMP WITH TIME ZONE, 
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notification_types (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL UNIQUE,
    delivery_channel notification_type_channel_enum NOT NULL,
    template_title VARCHAR(255) NOT NULL,
    template_body TEXT, 
    last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_notifications (
    id SERIAL PRIMARY KEY, 
    user_id BIGINT NOT NULL,
    type_id INT NOT NULL,

    metadata JSONB, -- dynamic data render in template body
    status user_notification_status_enum NOT NULL DEFAULT 'PENDING', 
    
    scheduled_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    sent_at TIMESTAMP,
    read_at TIMESTAMP,
    last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE user_goals (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  target_goal goal_target_enum NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  status goal_status_enum NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_partner_products (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  partner_product_id INT NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, partner_product_id)
);

-- Income Tables
CREATE TABLE income_payment_methods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE income_categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  user_id INT NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE income_transactions (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  transaction_date TIMESTAMP NOT NULL,
  name VARCHAR(255),
  amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
  category_id INT NOT NULL,
  currency_id INT NOT NULL,
  exclude_from_goal BOOLEAN DEFAULT FALSE,
  note TEXT,
  payment_method_id INT,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE income_transaction_attachments (
  id SERIAL PRIMARY KEY,
  transaction_id INT NOT NULL,
  filename VARCHAR(255) NOT NULL,
  path VARCHAR(1024) NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE income_planned_transactions (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  currency_id INT NOT NULL,
  day INT NOT NULL,
  "interval" income_interval_enum NOT NULL,
  start_date DATE NULL,
  end_date DATE NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Expense Tables
CREATE TABLE expense_payment_methods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense_categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  user_id INT NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense_transactions (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  transaction_datetime TIMESTAMP NOT NULL,
  name VARCHAR(255) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
  category_id INT NOT NULL,
  currency_id INT NOT NULL,
  exclude_from_goal BOOLEAN DEFAULT FALSE,
  note TEXT,
  payment_method_id INT,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense_transaction_attachments (
  id SERIAL PRIMARY KEY,
  transaction_id INT NOT NULL,
  filename VARCHAR(255) NOT NULL,
  file_type file_type_enum NOT NULL,
  content_length_bytes BIGINT NOT NULL CHECK (content_length_bytes < 10485760), -- 10MB limit
  path VARCHAR(1024) NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense_planned_transactions (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
  currency_id INT NOT NULL,
  day int NOT NULL,
  "interval" expense_interval_enum NOT NULL,
  start_date DATE NULL,
  end_date DATE NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense_planned_transaction_occurences (
  id SERIAL PRIMARY KEY,
  plan_id INT NOT NULL,
  transaction_id INT NULL,
  amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
  paid_date DATE NOT NULL,
  last_modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ------------------
-- 4. Apply Triggers for 'last_modified_at'
-- ------------------

CREATE TRIGGER set_timestamp_occupations BEFORE UPDATE ON occupations FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_work_experience_levels BEFORE UPDATE ON work_experience_levels FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_postal_codes BEFORE UPDATE ON postal_codes FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_education_levels BEFORE UPDATE ON education_levels FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_currencies BEFORE UPDATE ON currencies FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_partners BEFORE UPDATE ON partners FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_partner_products BEFORE UPDATE ON partner_products FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_users BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_user_subscriptions BEFORE UPDATE ON user_subscriptions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_user_goals BEFORE UPDATE ON user_goals FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_user_partner_products BEFORE UPDATE ON user_partner_products FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_income_payment_methods BEFORE UPDATE ON income_payment_methods FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_income_categories BEFORE UPDATE ON income_categories FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_income_transactions BEFORE UPDATE ON income_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_income_transaction_attachments BEFORE UPDATE ON income_transaction_attachments FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_income_planned_transactions BEFORE UPDATE ON income_planned_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_payment_methods BEFORE UPDATE ON expense_payment_methods FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_categories BEFORE UPDATE ON expense_categories FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_transactions BEFORE UPDATE ON expense_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_transaction_attachments BEFORE UPDATE ON expense_transaction_attachments FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_planned_transactions BEFORE UPDATE ON expense_planned_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_expense_planned_transaction_occurences BEFORE UPDATE ON expense_planned_transaction_occurences FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_subscription_plans BEFORE UPDATE ON subscription_plans FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_notification_types BEFORE UPDATE ON notification_types FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
CREATE TRIGGER set_timestamp_user_notifications BEFORE UPDATE ON user_notifications FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();


-- ------------------
-- 5. Add Foreign Key Constraints
-- ------------------

-- User Relationships
ALTER TABLE users ADD CONSTRAINT fk_users_occupation FOREIGN KEY (occupation_id) REFERENCES occupations(id);
ALTER TABLE users ADD CONSTRAINT fk_users_work_exp FOREIGN KEY (work_experience_level_id) REFERENCES work_experience_levels(id);
ALTER TABLE users ADD CONSTRAINT fk_users_edu_level FOREIGN KEY (education_level_id) REFERENCES education_levels(id);
ALTER TABLE users ADD CONSTRAINT fk_users_postal_code FOREIGN KEY (postal_code_id) REFERENCES postal_codes(id);
ALTER TABLE users ADD CONSTRAINT fk_users_currency FOREIGN KEY (currency_id) REFERENCES currencies(id);

ALTER TABLE user_subscriptions ADD CONSTRAINT fk_user_sub_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE user_goals ADD CONSTRAINT fk_user_goals_user FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE user_subscriptions ADD CONSTRAINT fk_user_sub_plan FOREIGN KEY (plan_id) REFERENCES subscription_plans(id);
ALTER TABLE user_notifications ADD CONSTRAINT fk_user_notif_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE user_notifications ADD CONSTRAINT fk_user_notif_type FOREIGN KEY (type_id) REFERENCES notification_types(id);


-- Income Relationships
ALTER TABLE income_categories ADD CONSTRAINT fk_income_cat_user FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE income_transactions ADD CONSTRAINT fk_income_trans_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE income_transactions ADD CONSTRAINT fk_income_trans_cat FOREIGN KEY (category_id) REFERENCES income_categories(id);
ALTER TABLE income_transactions ADD CONSTRAINT fk_income_trans_payment FOREIGN KEY (payment_method_id) REFERENCES income_payment_methods(id);
ALTER TABLE income_transactions ADD CONSTRAINT fk_income_trans_currency FOREIGN KEY (currency_id) REFERENCES currencies(id);

ALTER TABLE income_transaction_attachments ADD CONSTRAINT fk_income_attach_trans FOREIGN KEY (transaction_id) REFERENCES income_transactions(id);

ALTER TABLE income_planned_transactions ADD CONSTRAINT fk_income_plan_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE income_planned_transactions ADD CONSTRAINT fk_income_plan_cat FOREIGN KEY (category_id) REFERENCES income_categories(id);
ALTER TABLE income_planned_transactions ADD CONSTRAINT fk_income_plan_currency FOREIGN KEY (currency_id) REFERENCES currencies(id);

-- Expense Relationships
ALTER TABLE expense_categories ADD CONSTRAINT fk_exp_cat_user FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE expense_transactions ADD CONSTRAINT fk_exp_trans_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE expense_transactions ADD CONSTRAINT fk_exp_trans_cat FOREIGN KEY (category_id) REFERENCES expense_categories(id);
ALTER TABLE expense_transactions ADD CONSTRAINT fk_exp_trans_payment FOREIGN KEY (payment_method_id) REFERENCES expense_payment_methods(id);
ALTER TABLE expense_transactions ADD CONSTRAINT fk_exp_trans_currency FOREIGN KEY (currency_id) REFERENCES currencies(id);

ALTER TABLE expense_transaction_attachments ADD CONSTRAINT fk_exp_attach_trans FOREIGN KEY (transaction_id) REFERENCES expense_transactions(id);

ALTER TABLE expense_planned_transactions ADD CONSTRAINT fk_exp_plan_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE expense_planned_transactions ADD CONSTRAINT fk_exp_plan_cat FOREIGN KEY (category_id) REFERENCES expense_categories(id);
ALTER TABLE expense_planned_transactions ADD CONSTRAINT fk_exp_plan_currency FOREIGN KEY (currency_id) REFERENCES currencies(id);

ALTER TABLE expense_planned_transaction_occurences ADD CONSTRAINT fk_exp_occur_plan FOREIGN KEY (plan_id) REFERENCES expense_planned_transactions(id);
ALTER TABLE expense_planned_transaction_occurences ADD CONSTRAINT fk_exp_occur_trans FOREIGN KEY (transaction_id) REFERENCES expense_transactions(id) ON DELETE SET NULL;

-- Partner Relationships
ALTER TABLE partner_products ADD CONSTRAINT fk_partner_prod_partner FOREIGN KEY (partner_id) REFERENCES partners(id);

ALTER TABLE user_partner_products ADD CONSTRAINT fk_user_partner_user FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE user_partner_products ADD CONSTRAINT fk_user_partner_prod FOREIGN KEY (partner_product_id) REFERENCES partner_products(id);


COMMIT;
