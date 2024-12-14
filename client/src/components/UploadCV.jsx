import { useState } from 'react';
import { Box, Button, Typography } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes

const UploadCV = ({ onUpload }) => {
  const [fileName, setFileName] = useState('');
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {
      setFileName(file.name);
      setError('');
      onUpload(file); // Pass the file to the parent component
    } else {
      setError('Please upload a valid PDF file.');
      setFileName('');
      onUpload(null); // Clear the file in parent component if it's not valid
    }
  };

  return (
    <Box sx={{ marginBottom: '20px' }}>
      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        style={{ display: 'none' }}
        id="upload-file-input"
      />
      <label htmlFor="upload-file-input">
        <Button variant="contained" component="span">
          Upload CV
        </Button>
      </label>

      {fileName && (
        <Typography variant="body2" sx={{ marginTop: '10px' }}>
          Selected File: {fileName}
        </Typography>
      )}

      {error && (
        <Typography variant="body2" color="error" sx={{ marginTop: '10px' }}>
          {error}
        </Typography>
      )}
    </Box>
  );
};

// Define PropTypes for the UploadCV component
UploadCV.propTypes = {
  onUpload: PropTypes.func.isRequired, // onUpload is a required function
};

export default UploadCV;
