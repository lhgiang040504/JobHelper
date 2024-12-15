import { Card, CardContent, Typography, Box, IconButton } from '@mui/material';
import PropTypes from 'prop-types'; // Import PropTypes
import InfoIcon from '@mui/icons-material/Info';
import DeleteIcon from '@mui/icons-material/Delete';

const CandidateCard = ({ candidate, onViewDetails, onDelete }) => {
  return (
    <Card sx={{ maxWidth: '100%', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
      <CardContent sx={{ flexGrow: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}> 
    
          <Box sx={{marginBottom: 'auto' }}>
            <Typography variant="h7" gutterBottom sx={{ fontWeight: 'bold', marginBlock: "10px" }}>
              {candidate.contact.name}
            </Typography>
            <Typography variant="body2" color="textSecondary">
              Position: {candidate.role.name}
            </Typography>
            <Typography variant="body2" color="textSecondary">
              Experience: {candidate.role.num_experience}
            </Typography>
          </Box>

          <Box sx={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px'}} >
            <IconButton
              variant="contained"
              color='primary'
              size="small"
              onClick={() => onViewDetails(candidate._id)} // Gọi API chi tiết ứng viên
            >
              <InfoIcon/>
            </IconButton>
            <IconButton
              variant="contained"
              color="error"
              size="small"
              onClick={() => onDelete(candidate._id)} // Gọi API xóa ứng viên
            >
              <DeleteIcon/>
            </IconButton>
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
