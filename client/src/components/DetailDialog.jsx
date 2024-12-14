import { Dialog, DialogActions, DialogContent, DialogTitle, Button, Typography, Box, Grid } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes for validation

function DetailDialog({ open, onClose, candidateDetails }) {
  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Candidate Details</DialogTitle>
      <DialogContent>
        {candidateDetails ? (
          <Box>
            <Grid container spacing={2}>
              {/* Name */}
              <Grid item xs={12}>
                <Typography variant="h6">Name: {candidateDetails.contact.name}</Typography>
              </Grid>
              
              {/* Role */}
              <Grid item xs={12}>
                <Typography variant="body1">Position: {candidateDetails.role.name}</Typography>
              </Grid>
              <Grid item xs={12}>
                <Typography variant="body1">Experience: {candidateDetails.role.num_experience} years</Typography>
              </Grid>

              {/* Languages */}
              <Grid item xs={12}>
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
              <Grid item xs={12}>
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
          </Box>
        ) : (
          <Typography variant="body1">Loading...</Typography>
        )}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
}

// Prop validation using PropTypes
DetailDialog.propTypes = {
  open: PropTypes.bool.isRequired, // Indicates if the dialog is open
  onClose: PropTypes.func.isRequired, // Function to close the dialog
  candidateDetails: PropTypes.shape({
    contact: PropTypes.shape({
      name: PropTypes.string.isRequired,
    }).isRequired,
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
