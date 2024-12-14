import { Button, Card, CardContent, Typography, Box } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes

const CandidateCard = ({ candidate, onViewDetails, onDelete }) => {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          {candidate.contact.name}
        </Typography>
        <Typography variant="body2" color="textSecondary">
          Position: {candidate.role.name}
        </Typography>
        <Typography variant="body2" color="textSecondary">
          Experience: {candidate.role.num_experience}
        </Typography>

        <Box sx={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
          <Button
            variant="contained"
            size="small"
            onClick={() => onViewDetails(candidate._id)} // Gọi API chi tiết ứng viên
          >
            Detail
          </Button>
          <Button
            variant="contained"
            color="error"
            size="small"
            onClick={() => onDelete(candidate._id)} // Gọi API xóa ứng viên
          >
            Delete
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
};

// Định nghĩa PropTypes cho các props của component
CandidateCard.propTypes = {
  candidate: PropTypes.shape({
    _id: PropTypes.string.isRequired,
    contact: PropTypes.shape({
      name: PropTypes.string.isRequired,
    }).isRequired,
    role: PropTypes.shape({
      name: PropTypes.string.isRequired,
      num_experience: PropTypes.number.isRequired,
    }).isRequired,
  }).isRequired,
  onViewDetails: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default CandidateCard;
