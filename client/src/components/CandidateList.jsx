import { Grid } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes for validation
import CandidateCard from './CandidateCard';

const CandidateList = ({ candidates, onViewDetails, onDelete }) => {
  return (
    <Grid container spacing={2}>
      {candidates.map((candidate, index) => (
        <Grid item xs={12} sm={6} md={4} key={index}>
          <CandidateCard
            candidate={candidate}
            onViewDetails={onViewDetails}
            onDelete={onDelete}
          />
        </Grid>
      ))}
    </Grid>
  );
};

// Prop validation using PropTypes
CandidateList.propTypes = {
  candidates: PropTypes.arrayOf(
    PropTypes.shape({
      _id: PropTypes.string.isRequired, // Assuming '_id' is a unique identifier
      contact: PropTypes.shape({
        name: PropTypes.string.isRequired,
      }).isRequired,
      role: PropTypes.shape({
        name: PropTypes.string.isRequired,
        num_experience: PropTypes.number.isRequired,
      }).isRequired,
    })
  ).isRequired,
  onViewDetails: PropTypes.func.isRequired, // Function to view candidate details
  onDelete: PropTypes.func.isRequired, // Function to delete a candidate
};

export default CandidateList;
