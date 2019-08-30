/*
  Validation util helper that checks form validation
  elements with the given name and value of input element.
  Returns back any errors messages to use in the components.
*/
const validate = (name, value) => {
  switch (name) {
    case 'confirmation':
      if (value === '') {
        return {
          error: true,
          errMessage: 'Must enter in a confirmation.'
        };
      } else if (value.length !== 6) {
        return {
          error: true,
          errMessage: 'Confirmation must be 6 characters.'
        };
      }

      break;

    case 'firstname':
      if (value === '') {
        return {
          error: true,
          errMessage: 'Must enter in your first name.'
        };
      }

      break;

    case 'lastname':
      if (value === '') {
        return {
          error: true,
          errMessage: 'Must enter in your last name.'
        };
      }

      break;

    case 'email':
      // Regex to validate email
      const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

      if (value === '') {
        return { error: false, errMessage: '' };
      } else if (!emailRegex.test(value)) {
        return {
          error: true,
          errMessage: 'Must enter in a valid email address.'
        };
      }

      break;

    case 'phone':
      // Regex to validate US phone numbers only
      const phoneRegex = /^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})$/;

      if (value === '') {
        return { error: false, errMessage: '' };
      } else if (!phoneRegex.test(value)) {
        return {
          error: true,
          errMessage: 'Must enter in a valid phone number.'
        };
      }

      break;

    default:
      break;
  }

  return { error: false, errMessage: '' };
};

export default validate;
