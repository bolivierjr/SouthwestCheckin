const validate = state => {
  const { confirmation, firstname, lastname, phone, email } = state;
  const inputNames = { confirmation, firstname, lastname, phone, email };

  for (const [name, value] of Object.entries(inputNames)) {
    switch (name) {
      case 'confirmation':
        if (value === '') {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in a confirmation.'
          };
        } else if (value.length !== 6) {
          return {
            ...state,
            error: true,
            errMessage: 'Confirmation must be 6 characters.'
          };
        }

        break;

      case 'firstname':
        if (value === '') {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in your first name.'
          };
        }

        break;

      case 'lastname':
        if (value === '') {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in your last name.'
          };
        }

        break;

      case 'email':
        // Regex to validate email
        const emailRegex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

        if (value === '') {
          continue;
        } else if (!emailRegex.test(value)) {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in a valid email address.'
          };
        }

        break;

      case 'phone':
        // Regex to validate US phone numbers only
        const phoneRegex = /^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})$/;

        if (value === '') {
          continue;
        } else if (!phoneRegex.test(value)) {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in a valid phone number.'
          };
        }

        break;
    }
  }

  return { ...state, error: false };
};

export default validate;
