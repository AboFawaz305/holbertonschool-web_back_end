import assert from 'assert';
import readDatabase, { _atry } from '../utils';

const _try = (fn, ...args) => {
  try {
    return { isError: false, value: fn(...args) };
  } catch (e) {
    return { isError: true, value: e };
  }
};

export default class StudentsController {
  static async getAllStudents(_, res) {
    const dbPath = process.argv[2];
    const dbResult = await _atry(readDatabase, dbPath);
    if (dbResult.isError) {
      res.writeHead(500, {
        'Content-Type': 'text/plain',
      });
      res.end('Cannot load the database');
      return;
    }
    const db = dbResult.value;
    res.writeHead(200, {
      'Content-Type': 'text/plain',
    });
    const msg = ['This is the list of our students'];
    /* the db value contains the firsnames grouped by field
     * there is no other properties so I wont add an empty if
     * just because eslint said I should wrap the body of
     * a for in with an if
     */
    // eslint-disable-next-line guard-for-in
    for (const field in db) {
      msg.push(
        `Number of students in ${field}: ${db[field].length}. List: ${db[
          field
        ].join(', ')}`,
      );
    }
    res.end(msg.join('\n'));
  }

  static async getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const majorResult = _try(() => {
      const { major } = req.params;
      assert(major === 'CS' || major === 'SWE');
      return major;
    });
    if (majorResult.isError) {
      res.writeHead(500, {
        'Content-Type': 'text/plain',
      });
      res.end('Major parameter must be CS or SWE');
      return;
    }
    const dbResult = await _atry(readDatabase, dbPath);
    if (dbResult.isError) {
      res.writeHead(500, {
        'Content-Type': 'text/plain',
      });
      res.end('Cannot load the database');
      return;
    }
    const major = majorResult.value;
    const db = dbResult.value;
    res.writeHead(200, {
      'Content-Type': 'text/plain',
    });
    res.end(`List: ${db[major].join(', ')}`);
  }
}
