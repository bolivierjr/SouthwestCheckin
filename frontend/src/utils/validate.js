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

      case 'firstname':
        if (value === '') {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in your first name.'
          };
        }

      case 'lastname':
        if (value === '') {
          return {
            ...state,
            error: true,
            errMessage: 'Must enter in your last name'
          };
        }

      case 'email':
        if (value > 20) {
          return;
        }

      case 'phone':
        if (value > 20) {
          return;
        }
    }
  }

  return { ...state, error: false };
};

export default validate;
