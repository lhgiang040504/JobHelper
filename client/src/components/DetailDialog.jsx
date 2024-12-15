import { Dialog, DialogActions, DialogContent, DialogTitle, Button, Typography, Grid } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes for validation

function DetailDialog({ open, onClose, candidateDetails }) {
  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="md">
      <DialogTitle variant='h5'>Candidate Details</DialogTitle>
      <DialogContent>
        {candidateDetails ? (
          <Grid container spacing={2}>
            {/* Contact Details */}
            <Grid item xs={12} md={6}>
              <Typography variant="h6">Contact:</Typography>
              <Grid container spacing={1}>
                {Object.entries(candidateDetails.contact).map(([key, value], index) => (
                  <Grid item xs={12} key={index}>
                    <Typography variant="body1">
                      {key.charAt(0).toUpperCase() + key.slice(1)}: {value}
                    </Typography>
                  </Grid>
                ))}
              </Grid>
            </Grid>
            
            {/* Role */}
            <Grid item xs={12} md={6}>
              <Typography variant="h6">Role Information:</Typography>
              <Grid container spacing={1}>
                <Grid item xs={12}>
                  <Typography variant="body1">Position: {candidateDetails.role.name}</Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography variant="body1">Experience: {candidateDetails.role.num_experience} years</Typography>
                </Grid>
              </Grid>
            </Grid>

            {/* Languages */}
            <Grid item xs={12} md={6}>
              <Typography variant="h6">Languages:</Typography>
              <ul>
                {candidateDetails.language.map((lang, index) => (
                  <li key={index}>
                    <Typography variant="body1">{lang}</Typography>
                  </li>
                ))}
              </ul>
            </Grid>

            {/* Skills */}
            <Grid item xs={12} md={6}>
              <Typography variant="h6">Skills:</Typography>
              <ul>
                {candidateDetails.skills.map((skill, index) => (
                  <li key={index}>
                    <Typography variant="body1">{skill}</Typography>
                  </li>
                ))}
              </ul>
            </Grid>

            {/* Major */}
            <Grid item xs={12}>
              <Typography variant="h6">Major:</Typography>
              <ul>
                {candidateDetails.major.map((major, index) => (
                  <li key={index}>
                    <Typography variant="body1">{major}</Typography>
                  </li>
                ))}
              </ul>
            </Grid>
          </Grid>
        ) : (
          <Typography variant="body1">Loading...</Typography>
        )}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">Close</Button>
      </DialogActions>
    </Dialog>
  );
}

// Prop validation using PropTypes
DetailDialog.propTypes = {
  open: PropTypes.bool.isRequired, // Indicates if the dialog is open
  onClose: PropTypes.func.isRequired, // Function to close the dialog
  candidateDetails: PropTypes.shape({
    contact: PropTypes.object.isRequired, // Complete contact details
    role: PropTypes.shape({
      name: PropTypes.string.isRequired,
      num_experience: PropTypes.number.isRequired,
    }).isRequired,
    language: PropTypes.arrayOf(PropTypes.string).isRequired, // List of languages
    skills: PropTypes.arrayOf(PropTypes.string).isRequired, // List of skills
    major: PropTypes.arrayOf(PropTypes.string).isRequired, // List of majors
  }).isRequired,
};

export default DetailDialog;
