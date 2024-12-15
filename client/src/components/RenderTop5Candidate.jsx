import { Box, Card, CardContent, Typography, Grid } from "@mui/material";
import PropTypes from "prop-types";

function RenderTop5Candidate({ top5Candidates }) {
  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h6" gutterBottom>
        Top 5 Candidates
      </Typography>
      <Grid container spacing={2}>
        {top5Candidates.map((candidate) => (
          <Grid item xs={12} sm={6} md={4} key={candidate._id}>
            <Card
              sx={{
                maxWidth: "100%",
                height: "100%",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
              }}
            >
              <CardContent>
                <Typography variant="h6">{candidate.contact.name}</Typography>
                <Typography variant="body2" color="textSecondary" mt={1}>
                  Position: {candidate.role.name}
                </Typography>
                <Typography variant="body2" color="textSecondary" mt={1}>
                  Matching Skills:{" "}
                  {candidate.list_matching_skills.length > 0
                    ? candidate.list_matching_skills.join(", ")
                    : "No matching skills"}
                </Typography>
                <Typography variant="body2" color="#1E90FF" mt={1}>
                  Degree Score: {candidate.matching_degree_score}
                </Typography>
                <Typography variant="body2" color="#FF8C00" mt={1}>
                  Major Score: {candidate.matching_major_score}
                </Typography>
                <Typography variant="body2" color="red" mt={1}>
                  Skill Score: {candidate.matching_skill_score}
                </Typography>
                <Typography variant="body2" color="green" mt={1}>
                  Total Score: {candidate.total_score}
                </Typography>
                <Typography variant="body2" color="textSecondary" mt={1}>
                  File: {candidate.file_name}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}

RenderTop5Candidate.propTypes = {
  top5Candidates: PropTypes.array.isRequired,
};

export default RenderTop5Candidate;
