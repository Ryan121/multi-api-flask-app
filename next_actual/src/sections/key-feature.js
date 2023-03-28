/** @jsx jsx */
import { jsx } from 'theme-ui';
import { Container, Grid } from 'theme-ui';
import SectionHeader from '../components/section-header';
import FeatureCardColumn from 'components/feature-card-column.js';
import Performance from 'assets/key-feature/performance.svg';
import Partnership from 'assets/key-feature/partnership.svg';
import Subscription from 'assets/key-feature/subscription.svg';
import Support from 'assets/key-feature/support.svg';

const data = [
  {
    id: 1,
    imgSrc: Performance,
    altText: 'Education',
    title: 'Education',
    text:
      'PhD in Surgical Wearable Bio-robotics. Masters in Systems Engineering.',
  },
  {
    id: 2,
    imgSrc: Partnership,
    altText: 'Key Skills',
    title: 'Key Skills',
    text:
      'Python, Django, Tensorflow, AWS, SQL, Git, Terraform, Docker, Kubernetes, REST APIs, JavaScript, React.js, Power BI.',
  },
  {
    id: 3,
    imgSrc: Subscription,
    altText: 'Certifications',
    title: 'Certifications',
    text:
      'Certified in Azure, AWS & Google Cloud, Machine Learning, DevOps & Data Science.',
  },
  {
    id: 4,
    imgSrc: Support,
    altText: 'Projects',
    title: 'Projects',
    text:
      '10+ ML projects, 5+ Web Dev projects',
  },
];

export default function KeyFeature() {
  return (
    <section sx={{ variant: 'section.keyFeature' }} id="feature">
      <Container>
        <SectionHeader
          slogan="Key Skills and Experience"
          title="About Me"
        />

        <Grid sx={styles.grid}>
          {data.map((item) => (
            <FeatureCardColumn
              key={item.id}
              src={item.imgSrc}
              alt={item.altText}
              title={item.title}
              text={item.text}
            />
          ))}
        </Grid>
      </Container>
    </section>
  );
}

const styles = {
  grid: {
    width: ['100%', '80%', '100%'],
    mx: 'auto',
    gridGap: [
      '35px 0',
      null,
      '40px 40px',
      '50px 60px',
      '30px',
      '50px 40px',
      '55px 90px',
    ],
    gridTemplateColumns: [
      'repeat(1,1fr)',
      null,
      'repeat(2,1fr)',
      null,
      'repeat(4,1fr)',
    ],
  },
};
