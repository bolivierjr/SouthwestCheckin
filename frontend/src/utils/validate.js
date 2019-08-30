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
      const emailRegex = /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/;

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
